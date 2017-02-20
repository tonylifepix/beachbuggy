import types
from bs4 import BeautifulSoup
import codecs
import urllib.request
import re
import xml.dom 

def create_element(doc,tag,attr):
    elementNode=doc.createElement(tag)
    textNode=doc.createTextNode(attr)
    elementNode.appendChild(textNode)
    return elementNode

newsall="    "
dom1=xml.dom.getDOMImplementation()
doc=dom1.createDocument(None,"news",None)
top_element = doc.documentElement
url = "http://wap.ithome.com/it/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"html5lib")
newsg = soup.find_all("span", class_="title")
for child in newsg:
        if child != "" :
                newsall = newsall + " 🔷 " + str(child.string)
sNode=doc.createElement('span')
headNode=create_element(doc,'head',newsall)
sNode.appendChild(headNode)
top_element.appendChild(sNode)
xmlfile=codecs.open('news.xml','w','utf-8')
doc.writexml(xmlfile,addindent=' '*4, newl='\n', encoding='utf-8')
xmlfile.close()
