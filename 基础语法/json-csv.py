#JSON 字符串只能用"    load dump 与文件操作相关 loads dumps 与文件操作无关
 
import json

persons=[
    {
        'name':'李白',
        'age':'25'
    },
    {
        'name':'苏轼',
        'age':'27'
    }
]
# json_str = json.dumps(persons,ensure_ascii=False)
# with open('person.json','w',encoding='utf-8') as fp:
#     fp.write(json_str)

# with open('person2.json','w',encoding="utf-8") as fp:
#     json.dump(persons,fp,ensure_ascii=False)

# with open('person2.json','r',encoding="utf-8") as fp:
#     json_str = json.load(fp)
# print(json_str)
# json_info ='[{"name": "李白", "age": "25"}, {"name": "苏轼", "age": "27"}]'#要将json格式变成str
# python_str = json.loads(json_info,encoding='utf-8')
# print(python_str,json_info)  

import csv
with open('stock.csv') as fp:
    reader = csv.read(fp) 
