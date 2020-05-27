import requests
from bs4 import BeautifulSoup

url = "https://www.umei.cc/p/gaoqing/cn/"
response = requests.get(url=url,)
response.encoding="utf-8"
text = response.text

soup = BeautifulSoup(text,"lxml")
"""
find(标签，atrris={"属性":"值"})
find_all( 标签，atrris={"属性":"值"} ) 
"""
alist = soup.find("div",attrs={"class":"TypeList"}).find_all('a',attrs={"class":"TypeBigPics"})

for a in alist:
    href = a.get("href")
    child_resp=requests.get(url=href)
    child_resp.encoding="utf-8"
    child_soup=BeautifulSoup(child_resp.text,"lxml")
    img_html = child_soup.find('div',attrs={"id":"ArticleId0"}).find("img")
    pic_title = child_soup.find("div",attrs={"class":'ArticleTitle'}).strong.text
    with open("%s.jpg"%pic_title,"wb") as fb:
        fb.write(requests.get(img_html.get("src")).content)
        print(1)

    
    

    


