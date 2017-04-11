
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[86]:

data = DataFrame(np.arange(16).reshape((4,4)), index = ['OH','OR','CA','WA'], columns = ['One','Two','Three','Four'])
data


# In[88]:

data.drop(['OR','CA'])


# In[89]:

data.drop(['Two','Four'], axis=1)


# In[18]:

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj


# In[19]:

obj['b']


# In[20]:

obj[1]


# In[21]:

obj[2:4]


# In[23]:

obj[['b','a','d']]


# In[24]:

obj[[1,3]]


# In[25]:

obj[obj<2]


# In[31]:

obj['b':'c'] = 5
obj


# In[32]:

data = DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado','Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
data


# In[34]:

data['two']


# In[35]:

data[['three','one']]


# In[36]:

data[:2]


# In[37]:

data[data['three']>5]


# In[38]:

data<5


# In[39]:

data[data<5] = 0


# In[40]:

data


# In[41]:

data.ix['Colorado','two']


# In[44]:

data.ix[['Colorado','Ohio']]


# In[45]:

data.ix[2]


# In[46]:

data.ix[:'Utah', 'two']


# In[47]:

data.ix[data.three > 5, :3]


# In[48]:

#obj.ix[:val] 选取单个列
# icol,irow 根据整数位置选取单列或单行，并返回一个Series
#get_value, set_value 根据行标签和列标签选取和设置单个值


# In[49]:

#pandas最重要的一个功能是，它可以对不同索引的对象进行算术运算。在将对象相加时，如果存在不同的索引对，则结果的索引就是该索引对的并集。我们来看一个简单的例子
s1 = Series([7.3,-2.5,3.4,1.5], index = ['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1 + s2


# In[50]:

#把它们相加后将会返回一个新的DataFrame，其索引和列为原来那两个DataFrame的并集
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1 + df2


# In[54]:

df1


# In[56]:

df2


# In[57]:

#使用df1的add方法，传入df2以及一个fill_value参数
df1.add(df2, fill_value= 0)


# In[ ]:

#+-×/  add, sub, div, mul


# In[59]:

#这就叫做广播（broadcasting）
arr = np.arange(12).reshape((3,4))
arr


# In[60]:

arr - arr[0]


# In[61]:

arr - arr[2]


# In[62]:

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index= ['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
frame -series


# In[63]:

series2 = Series(range(3), index=['b', 'e', 'f'])
series2


# In[64]:

frame - series2


# In[69]:

series3 = frame['d']
series3


# In[92]:

frame.sub(series3, axis = 0)


# In[94]:

#NumPy的ufuncs（元素级数组方法）也可用于操作pandas对象
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame


# In[95]:

np.abs(frame)


# In[97]:

#另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上
f= lambda x: x.max() - x.min()
frame.apply(f, axis =1)


# In[99]:

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index= ['Utah', 'Ohio', 'Texas', 'Oregon'])
frame


# In[103]:

np.sum(frame,axis = 1)


# In[105]:

np.sum(frame,axis = 0)


# In[106]:

np.mean(frame)


# In[108]:

np.mean(frame,axis = 1)


# In[111]:

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f, axis = 1)


# In[113]:

format = lambda x: '%.2f' %x
frame.applymap(format)


# In[114]:

#Series有一个用于应用元素级函数的map
frame['e'].map(format)


# In[116]:

#根据series的index进行排序
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()


# In[117]:

#而对于DataFrame，则可以根据任意一个轴上的索引进行排序
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()


# In[118]:

frame.sort_index(axis = 1)


# In[120]:

#数据默认是按升序排序的，但也可以降序排序
frame.sort_index(axis = 1, ascending = False)


# In[3]:

#对值进行排序 使用order的方法, 所有NaN都会排到末尾
obj = Series([4, 7, -3, 2])
obj.order()


# In[4]:

obj = Series([4, 7, -3, 2])
obj.sort_values()


# In[ ]:



