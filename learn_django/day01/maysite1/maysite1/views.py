from django.http import HttpResponse

def pages_view(request,pag):
    
    html = "这是第%s个标签"%pag
    return HttpResponse(html)

def page_2003_view(request):
    html = '<h1>这是第一个页面</h1>'
    return HttpResponse(html) 
# def func_view(request,num1,func,num2):
#     # if func not in ["add","sub","mul"]:
#     #     return HttpResponse('输入错误')
    
#     num1=int(num1)
#     num2=int(num2)
#     if func == 'add':
#         result = num1+num2
        
#     elif func == 'sub':
#         result = num1-num2
        
#     elif func == 'mul':
#         result = num1*num2
#     else:
#         result = "输入有误"
#     return HttpResponse('result is %s'%result)
def birthday_view(request,year,month,day,birthday):
    year = int(year)
    month = int(month)
    day = int(day)
       
    return HttpResponse("生日是%d年%d月%d日"%(year,month,day))
