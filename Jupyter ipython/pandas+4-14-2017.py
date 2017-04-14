
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series


# In[3]:

range(7, 0, -1)


# In[4]:

frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two','two', 'two', 'two'],  'd': [0, 1, 2, 0, 1, 2, 3]})


# In[5]:

frame


# In[11]:

frame2= frame.set_index(['c','b'])#以某一列或多列为index 
frame2


# In[13]:

frame3 = frame.set_index('b', drop = False) #默认index会从表中移除 可以改动嘛
frame3


# In[19]:

frame4=frame2.stack()#压缩成Series
frame4


# In[18]:

type(frame4)


# In[20]:

frame2.reset_index()#打回原形 和set_index正好想反


# In[24]:

ser = Series(np.arange(3.))
ser


# In[25]:

ser[-1]#整数索引不能用这个 有歧义


# In[26]:

ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2


# In[27]:

ser2[-1]#非整数索引就可以用


# In[33]:

ser3 = Series(range(1,4), index=[-5, 1, 3])
ser3.iget_value(2)


# In[34]:

ser3.iloc[0]#根据整数索引值取得value


# In[35]:

ser3.iat[0]


# In[44]:

frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
frame


# In[38]:

frame.iloc[1]


# In[41]:

frame.icol(1)


# In[45]:

frame.iloc[:,0]


# In[54]:

import pandas_datareader.data as web


# In[55]:

pdata= pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009','6/1/2012')) for stk in ['AAPL','GOOG','MSFT','DELL']))


# In[70]:

pdata.to_frame()


# In[58]:

pdata.ix[:,'6/1/2012',:]


# In[68]:

pdata.ix[:, '5/22/2012':,:]


# In[69]:

stacked= pdata.ix[:, '5/22/2012':,:].to_frame()#to_frame 转换成表格
stacked


# In[ ]:

'''
load 文件
read_cvs 从文件，URL，文件性对象中加载带分隔符的数据，默认分隔符逗号
read_table 从文件，URL，文件性对象中加载带分隔符的数据，默认分隔符为制表符‘/t’
read_fwf 读取定宽列格式数据（也就是说没有分隔符）
read_clipboard 读取剪贴板中的数据，可以看作read_table的剪贴板'''

