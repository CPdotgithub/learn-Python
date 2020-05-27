import sys
import os
# sys.setrecursionlimit(4000)
# def fun(i):
#     print(i)
#     fun(i+1)
# fun(1)

# 递归的作用
""""
 遍历文件夹,所有子文件
"""

# def run(path):
#     lst = os.listdir(path)
#     for name in lst:#拿到文件名
#         real_path = os.path.join(path,name) 
#         if os.path.isfile(name):

#             print(name)
#         else:
#             run(real_path)

path = 'D:\\Github\\CPdotgithub\\Python\\study code\\learn-Python'
files = os.listdir(path)

for file in files:
    real_path = os.path.join(path,file)
    if os.path.isfile(real_path):
        print(file)
    else:
        pass