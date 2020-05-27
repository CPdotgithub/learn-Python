import pandas as pd 

df = pd.read_csv('./data.csv',header=None)
red_ball = df.loc[:,1:6]# 先行后列
red_counts = pd.value_counts(red_ball.values.flatten())#给一维数据排序
blue_ball = df.loc[:,[7]]
blue_counts = pd.value_counts(blue_ball.values.flatten())



import matplotlib.pyplot as plot

plot.pie(red_counts,labels=red_counts.index)
plot.show()

