
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

datadict = {}
url = 'https://github.com/shraddhabarke/Phonosynthesis/tree/master/datasets'
uClient = uReq(url)
html = uClient.read()
uClient.close()
page_soup = soup(html, "html.parser")
containers = page_soup.findAll("tr",{"class":"js-navigation-item"})
del containers[0]
for container in containers:
    datadict.update({container.a["title"]:container.a["href"]})




