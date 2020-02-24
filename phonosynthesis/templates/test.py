import os
os.getcwd()
path = os.path.join("../datasets/" + "riggle.csv")
f = open(path,"r")
content = f.read()
print(content)
