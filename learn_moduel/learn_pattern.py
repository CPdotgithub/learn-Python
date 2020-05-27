import re

# match 只会在开始进行查询



# search 整个字符串查询


# group  匹配正则表达式中（num）的内容  group(0)为整个正则表达式  group（1，2）指定多个分组  groups（）拿出所有子分组
text = " Apple's price $99 , orange's price is $10 . "
ret = re.search("\.*(\$\d+).*(\$\d+)",text)
print(ret.group(1,2))
for i in range(1,3):
    if i % 2 != 0 :
        resp = ret[i]+ret[i+1]
        print(resp)










#findall
# text = " Apple's price $99 , orange's price is $10 . "
# ret = re.findall('\$\d+',text)
# print(ret)


#sub替换
#text = " Apple's price $99 , orange's price is $10 . "
# ret = re.sub('\$\d+',"不要钱",text)
# print(ret)

# split分割
# text = " Apple's price $99 , orange's price is $10 . "
# # ret = re.split(' |,',text)
# ret = re.split('[^a-z]',text)
# print(ret)

#compile 
# text = 'the number is 20.50'
# r = re.compile(r"""
#     \d+ #小数点前的数字
#     \.? #小数点
#     \d* #小数点后面的数字
# """,re.VERBOSE)
# ret = re.search(r,text)
# print(ret.group)