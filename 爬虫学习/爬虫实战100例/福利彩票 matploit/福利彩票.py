import requests
from lxml import etree
import pandas as pd

 #etree.HTML 把字符串解析成 HTML 文件
 #html = etree.HTML(text)
 #s = etree.tostring(html).decode()

url = "http://datachart.500.com/ssq/history/newinc/history.php?limit=10000&sort=0"

response = requests.get(url)
response.encoding="GBK"

hm = etree.HTML(response.text)
trs = hm.xpath('//tbody[@id="tdata"]/tr')
f = open('data.csv',mode='w')
for tr in trs:
    tds=tr.xpath('td/text()')
    #删除数据中的' ',','
    m = map(lambda x: x.replace(',','').replace('\xa0',''),tds)
    
    #准备写入csv
    #csv-> pandas
    s = ','.join(m)
    f.write(s+'\n')



