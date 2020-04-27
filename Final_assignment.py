import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

os.mkdir('Shikha')
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
i=1
soup = make_soup("https://www.worldblaze.in/19-official-websites-of-bollywood-actresses-actors/")
for img in soup.findAll('img'):
    temp = img.get('src')
    if temp[:1]=="/":
        image = "https://www.worldblaze.in/19-official-websites-of-bollywood-actresses-actors/" + temp
    else:
        image = temp
   
    nametemp = img.get('alt')
    if len(nametemp) != 0:
        filename=nametemp
        imagefile = open("shikha\\" +filename + ".jpeg",'wb')
        
        imagefile.write(urllib.request.urlopen(image).read())
        
        imagefile.close()
containers=soup.find("div",{"class":"thecontent"})
paragraph1=[]
paragraph1=containers.findAll('p')
paragraph1.append('a')
heads=containers.findAll('strong')
para=0
for para in paragraph1[1::2]:
    textfile=open("shikha\\"+".txt",'a')
    textfile.write(para.text)
    textfile.write("\n\n")
    textfile.write(heads[i].text)
    textfile.write("\n")
    textfile.close()
    i+=1