# from bs4 import BeautifulSoup
# import requests
# import os
# import time

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     'Cookie': '__51cke__=; bdshare_firstime=1590123284725; __tins__18804156=%7B%22sid%22%3A%201590123284620%2C%20%22vd%22%3A%209%2C%20%22expires%22%3A%201590125220339%7D; __51laig__=9',

# }
# page_num = [' ']
# page_num.extend(range(2,26))

# for num in page_num:
#     page_url = "http://www.kuuxoo.com/riben/134.html"
#     if num==" ":
#         pass
#     else:
#         page_url = "http://www.kuuxoo.com/riben/134_%d.html"%num
    
#     response = requests.get(url=page_url,headers=headers)
#     response.encoding="GBK"
#     text = response.text
#     soup = BeautifulSoup(text,'lxml')
#     pic_page = soup.find('div', attrs={'id':"content",'class':"content"}).find('img')
#     pic_url = pic_page.get('src')
    
#     pic_title =soup.find('div',attrs={'class':'title'}).h1.text
#     img_response = requests.get(pic_url)
#     img_response.encoding="GBK"
#     img = img_response.content
#     with open('%s.jpg'%pic_title,"wb") as fp:
        
#         fp.write(img)
#         time.sleep(0.5)
