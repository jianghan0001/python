
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
import pandas_datareader as pdd


# In[5]:

data = Series([1, np.NaN, 3.5, np.NaN, 7])
data


# In[8]:

s= data.dropna()
s


# In[10]:

#通过布尔型索引达到这个目的
s= data[data.notnull()]
s


# In[13]:

#dropna 默认丢弃行 drop列使用axis = 1
data = DataFrame([[1., 6.5, 3.], [1., np.NaN, np.NaN], [np.NaN, np.NaN, np.NaN], [np.NaN, 6.5, 3.]])
data


# In[14]:

data.dropna()


# In[15]:

data.dropna(axis = 1)


# In[20]:

data.dropna(how = 'all')#只丢弃全为NaN的行


# In[26]:

data.dropna( how = 'all',axis = 1) #列


# In[31]:

df =DataFrame(np.random.randn(7,3))
df


# In[33]:

df.ix[:4, 1]= np.NaN
df.ix[:2, 2] = np.NaN


# In[34]:

df


# In[43]:

data.dropna(thresh= 3)


# In[65]:

raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
        'age': [42, np.nan, 36, 24, 73],
        'sex': ['m', np.nan, 'f', 'm', 'f'],
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])
df


# In[50]:

df.dropna(thresh = 5)


# In[66]:

df['location']= np.nan


# In[52]:

df


# In[53]:

df.dropna(how = 'any')


# In[54]:

df.dropna(how = 'all')


# In[55]:

df.dropna(how = 'all', axis = 1)


# In[56]:

df.fillna(0)


# In[67]:

df["preTestScore"].fillna(df.groupby("sex")["preTestScore"].transform("mean"), inplace=True)
df


# In[68]:

df[df.sex.notnull() & df.postTestScore.notnull()]


# In[69]:

df


# In[71]:

df.fillna(method = 'ffill')


# In[73]:

df.location[1] =0


# In[74]:

df


# In[76]:

df.fillna(method = 'ffill', limit = 2)


# In[90]:

df.ix[3, 3] #索引要用ix ix ix 不用ix显示的是列 列 列


# In[91]:

data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])


# In[92]:

data


# In[94]:

data.index


# In[96]:

data[:, 3]


# In[97]:

data.unstack()#多重排序 转换成表格 加维度


# In[98]:

data.unstack().stack()


# In[99]:

frame = DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])


# In[100]:

frame


# In[104]:

frame.index.names = ['key1' , 'key2']#加名字


# In[105]:

frame.columns.names = ['state', 'color']


# In[106]:

frame


# In[108]:

frame['Ohio']


# In[109]:

frame.swaplevel('key1', 'key2') #index互换


# In[111]:

frame


# In[118]:

frame.sortlevel(1)# 按某一index排序 默认0


# In[114]:

frame.swaplevel(0,1).sortlevel() 


# In[116]:

frame


# In[115]:

frame.sum(level='key2') #许多对DataFrame和Series的描述和汇总统计都有一个level选项，它用于指定在某条轴上求和, 可以分级别 和groupby一回事


# In[ ]:



