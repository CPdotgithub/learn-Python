import re 
"""
常用方法:
match   : 从开头开始匹配
search  : 整个字符串匹配
compile : 生成需要匹配的内容
findall : 匹配所有

"""
mystr = '<script src="chrome-search://local-ntp/animations.js"integrity="sha256-1+GSDjMMklBjZY0QiWq+tGupCvajw4Xbn46ect2mZgM="></script>'
restr = re.compile(r'/(/.*)"integrity')
reg = re.findall(restr,mystr)
print(reg)