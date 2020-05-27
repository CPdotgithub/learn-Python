**创建项目** 
======
   mkdir file_name   
   cd file_name  
   django-admin startproject  project_name

## **URL(统一资源定位符)**
一般语法格式为 
protocol(协议) ://hostname[:port]/path [?query][#fragment]
[非必须项]

# **path转化器**
|转换器|效果|例子|
|:--:|:--:|:--:|
|str|匹配除了"/"之外的非空字符串|\<str:index>|
|int|匹配0和任何正整数|\<int:num>|
|slug|ASCII编码字符串|\<slug:sl>|
|path|非空字段包括""/|\<path:ph>|



