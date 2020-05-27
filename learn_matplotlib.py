import matplotlib   
import matplotlib.pyplot as plt #模块pyplot包含生成图表函数
squares=[val**2 for val in range(1,11)]
values=
plt.plot(squares,linewidth=5)#linewidth 绘图线条粗细

plt.title("squares numbers".title(),fontsize=25)#fontsize 字体大小
plt.xlabel("val".title(),fontsize=14)#.xlabel()给x轴打标签
plt.ylabel("Squares of Val",fontsize=14)

plt.tick_params(axis="both",labelsize=14)

plt.show()#    --snip--省略代码
