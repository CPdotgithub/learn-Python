import  numpy as np 
import  pandas as pd 
import matplotlib.pyplot as plot 
import tushare as ts 

df = ts.get_k_data('600519',start='1988-01-01')
df.to_csv('600519.csv')
print(df)
#df = pd.read_csv('600519.csv',index_col='data',parse_dates=[])
