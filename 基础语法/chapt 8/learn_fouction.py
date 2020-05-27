"""求阶乘factorial"""
# import time
# start_time=time.time()
# def fac(num):
#     result=1
#     while num>=1:
#         result *=num
#         num-=1
#     return result
# end_time=time.time()
# print(end_time-start_time)
# print(fac(int(input("Enter a number"))))


"""实现计算求最大公约数和最小公倍数的函数"""
# def gcd(num1,num2):
#     for factor in range(num1,0,-1):#不包含0
#         if num1%factor==0 and num2%factor==0 :
#             return  factor

# def gys(num1,num2):
#     result=num1*num2//gcd(num1,num2)   #/ result返回浮点值 //返回整数值
#     return result   #只返回result的值  不返回变量名
# gcd_result=gcd(16,4)
# gys_result=gys(16,4)

# print(gcd_result,gys_result)
# if result==1:
#     print("两个数互质") 

"""实现判断一个数是不是回文数的函数。"""
num=int(input("number:"))
tem_num=num
reversed_num=0
while tem_num>0:
    tem_num//=10
    reversed_num=reversed_num*10+tem_num%10
print(reversed_num)
    
