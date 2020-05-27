# *ls*当前文件目录
## -a[all] 查看所有文件 包括隐藏文件
## -l[long] -lh 显示详细信息
![详细信息](pic\QQ拼音截图20200522000655.png)
### drwxr-xr-x     
### 开头-[二进制文件] d[文件目录] l [link软连接] rwx 表示u所有者权限 r-x表示g组权限 o其他人权限  r 读 w写 x执行 - 没有该权限

# *mkdir* *rmdir*
# *cp [-rp -r复制目录 -p保留属性同步更新 创建时间等] /path  /dir_path/newname*

# mv /path/fb /dirpath、newname  
    剪切功能  不需要-r  不添加path 在当前目录下 可当做改名使用
# rm 删除文件 -f 直接删除不放入回收站
## rm -r /path 删除目录  不需要确认 -rf
# touch [/path/文件名]  
    文件名之间空格 创建两个文件 "file name" 可以创建带空格的文件

# cat 
    浏览文件内容  
# more 
    分页显示内容  空格 F 页下翻  enter行下翻
# less 
    可以上翻 pageup 页上翻  上箭头 行上翻
# head -n  
    查看前n行  默认前十行
# tail -n  
    查看后n行  默认后十行
## tail -f 
    动态显示后十行
# ln
    链接文件 命令
    软连接(类似于快捷方式可以跨分区) 
    ln -s /path/file  /path2/file.soft
    硬链接(不能跨分区不允许指定目录) 
    ln  /path/file /path2/file.hard
    ln -i file_name 查看文件节点ID 


# 权限管理命令
## *chmod*
    chmod[{ugoa}{+-=}{rwx}][文件目录名] 
    r - 4 w - 2 x - 1
    rwx 7 rw 6 r-- 4
    chmod 641 file-name
    chmod -R file-name [改变该目录下所有子文件权限]
    file      
        r : cat/more/head/tail/less
        w : vim
        x : script command
    
    dirctory  
        r : ls
        w : touch/mkdir/rmdir/rm
              
# chown username directory-filename
# chgrp groupname directory-filename


# find 文件搜索 
    find / -name filename
    find / -name *adc* (文件名包含adc都会被搜索出来)
    find / -name adc*,adc??? (查找以adc开头文件 ?匹配单个字符)
    find / -iname  file-name (不区分大小写)
    find / -size [+-=]n   (大于小于等于数据块 1=512字节 0.5k)
    find / -user usernam  所有者所有文件
    find / -group  groupname
    find / -cmin -5(分钟)
           -amin : 访问时间 access
           -cmin : 文件属性 change
           -mmin : 文件内容 modify
    find -a(and) -o(or) 
    find / -size +100 -a -size -1000
    -type f(文件) d(目录) l(软连接)
    find / -name filename -exec ls -l {} \;   
        查找文件并直接执行
    - inumber 根据节点查找
    locate
    which 查找路径 别名
    grep  文件内容查找
    grep -v  ^# 排除#号开头
 