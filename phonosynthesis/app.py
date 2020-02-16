from flask import Flask, abort, jsonify, request, render_template
from phonosynthesis import ipa_data
from phonosynthesis import phonosynth
from pathlib import Path
import os


app = Flask(__name__, static_url_path='')
app.config.from_envvar('PHONOSYNTHESIS_CONFIG')

@app.route('/')
def handle_homepage():
  address = []
  fileName = []
  for root, dirs, files in os.walk('./datasets'):
    for file in files:
        address.append(os.path.join(root,file))
        fileName.append(file.replace('.csv',''))
  return render_template('index.html',address = address, fileName = fileName)

@app.route('/api/infer_rule', methods=['POST'])
def handle_infer_rule():
  if not request.json or not 'wordStems' in request.json:
    abort(400)

  words = []
  for stem in request.json['wordStems']:
    words.append((stem['underlyingForm'], stem['realization']))

  return jsonify(infer_rule(words))

def format_features(features):
  matching_letter = ipa_data.get_matching_letter(features)
  if matching_letter:
    return matching_letter
  elif len(features) == 0:
    return None
  else:
    return [{'feature': feature, 'value': value} for feature, value in features.items()]

def infer_rule(words):
  data = phonosynth.parse(words)
  change = phonosynth.infer_change(data)
  rules = phonosynth.infer_rule(data, change)
  response = []
  for rule in rules:
    if rule:
      change, (left, target, right) = rule
      response.append(ipa_data.format_rule(target, {'left': left, 'right': right}, change))
  return response
