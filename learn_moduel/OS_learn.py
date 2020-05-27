import os

#print(os.sep,os.name,os.getenv('os'),os.getcwd())
"""
sep分隔符
name 系统
getenv 环境变量
getcwd 当前工作环境

"""

dirs = "D:\\Github\\CPdotgithub\\Python\\study code\\learn-Python"
# files = os.listdir(dirs)
# os.path.isfile(files)#判断是否为文件
# os.path.isdir(files)
# os.path.exists(files)
# os.makedirs()
# os.removedirs()
# os.chdir(): 改变当前目录到指定目录中
# os.rename()



del_dir = 'D:\\Github\\CPdotgithub\\Python\\study123'
os.rmdir(del_dir)

