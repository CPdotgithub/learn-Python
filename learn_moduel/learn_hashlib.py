"""hash 算法输出相同 hash碰撞
   hash（） 当前进程 唯一

MD5   密码杂凑函数 128  hash  value 数字指纹

 1.压缩性
 2.容易计算
 3.抗修改性
 4.强碰撞性 



"""
import hashlib
m = hashlib.md5
m.update(b'hello world !') #md5加密  md5 只能bites b  str  只能ASCii  "zhongern".encode("utf-8") 


print(m.digest())
print(m.hexdigest()) #16进制

"""
hash-sha-1  160位

目前流行 sha-256

ssl
ssl2网站加密

md5 文件校验
sha-256 加密

"""

