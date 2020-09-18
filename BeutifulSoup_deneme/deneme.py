import requests
from bs4 import BeautifulSoup

#my user agent
robotum={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

sahibinden=requests.get("https://www.sahibinden.com/",headers=robotum)

#print(sahibinden.status_code)
icerik=sahibinden.content

soup=BeautifulSoup(icerik,"html.parser")
print(soup.title.text)

if len(soup.title.text) > 60:
    print("Title 60 karakterden fazla, kısaltmayı deneyin!!!")

h1=soup.find("h1")
#print(h1)

h1all=soup.find_all("h1")
#print(h1all)
#print(len(h1all))

if len(h1all) > 1:
    print("h1 başlığı sayısı 1'den fazla")

linkler=soup.find_all("a")
#print(len(linkler),"adet link")
#print(linkler)

basliklar=soup.find_all("div",{"class":"item column-1"})
#print(len(basliklar))
for baslik in basliklar:
    print(baslik.h2.a.text)

gorseller=soup.find_all("img")
gorselleralt=soup.find_all(alt=True)

imgcount=len(gorseller)
imgaltcount=len(gorselleralt)
alterror=imgcount-imgaltcount
#print(alterror,"görselde alt etiketi yok")

sec=soup.select("p > a")
#print(sec)

htmlcount=len(icerik)
#print(htmlcount)

paragraf=soup.select("p")
paragrafcount=0
for metin in paragraf:
    paragrafcount+=len(metin.text)

#print(paragrafcount/htmlcount*100)

menu=soup.select("nav > ul > li > a")
for item in menu:
    print(item.text)

dropdownmenu=soup.select("nav > ul > li > ul > li > a")
for dropitem in dropdownmenu:
    print(dropitem.text)



