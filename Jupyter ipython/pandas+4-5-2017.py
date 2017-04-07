
# coding: utf-8

# In[1]:

'''
# padas 是python里的sql 运行在memery上 快
# dataframe2维  series序列1维  panel 3维
# read_table('abc.csv', sep= ',', header = 1, index_col = 0, na_value = '-', parse_dates = True) (,分割， header为1， -为NaN， )
%matplotlib inline #不产生新窗口 
sep = "\s+" #空格分割  空格无限长
names = ['year', 'mean temo']
index_col = 0 以第一列为index
parse_dates = True  让日期变为日期格式
func括号内按shift 有提示
'''


# In[3]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[5]:

obj= Series([1, 'a', 1.1, np.pi])
obj


# In[6]:

obj[1]


# In[10]:

obj.values


# In[16]:

np.array(obj.index)


# In[17]:

ojb2= Series ([3,5,6,8], index = ['a', 'c', 'd', 'e'])
ojb2


# In[18]:

ojb2.index


# In[20]:

ojb2['a']


# In[25]:

ojb2[['e', 'a']]#一定是2个括号


# In[26]:

ojb2[ojb2>5]


# In[27]:

ojb2*2


# In[28]:

np.exp(ojb2)


# In[35]:

#可以将Series看成是一个定长的有序字典 因为它有一个索引值到数据值得映射
'a' in ojb2 #只可以检索key值


# In[32]:

ojb2


# In[46]:

sdata = {'OR': 1, 'NH' : 2, 'DE' :3}
obj3= Series(sdata)
obj3


# In[48]:

#isnull/notnull 检测NaN
state = ['DE','OR', 'CA','NH']
obj4=Series(obj3, index = state)
obj4


# In[49]:

pd.isnull(obj4)


# In[50]:

pd.notnull(obj4)


# In[51]:

obj4 +obj3 #相同索引值自动对应


# In[52]:

obj4.name = 'population'
obj4.index.name = 'state'
obj4


# In[55]:

#索引可以通过赋值的方式就地改变
ojb2.index = [5,5,5,5]
ojb2


# In[56]:

#DataFrame 表表表
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001,2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame


# In[71]:

#可以指定列的顺序
frame2= DataFrame(data, columns = ['year', 'state', 'pop','debt'], index= ['one', 'two', 'three', 'four','five'])
frame2


# In[73]:

frame2.columns#读取都有啥列


# In[74]:

frame2['state']#读取某一列


# In[77]:

frame2.year#另一种写法


# In[79]:

frame2.ix['three']#通过索引调取某一行 index是列名


# In[80]:

frame2.debt = 10.5#通过赋值进行修改
frame2


# In[83]:

frame2.debt = np.arange(5)
frame2


# In[88]:

val = Series([-1, -3, 5], index = ['two', 'four', 'five'])
frame2.debt = val
frame2#相同索引值填充， 不够的填NaN


# In[92]:

frame2['eastern'] = frame2.state == 'Ohio'#给一个不存在的列赋值会产生一个新的列 记住给新列赋值只能用中括号
frame2


# In[ ]: have a rest



