
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame


# In[2]:

lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),  index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],[2001, 2000, 2000, 2000, 2001, 2002]],columns=['event1', 'event2'])


# In[3]:

lefth


# In[4]:

righth


# In[5]:

pd.merge(lefth, righth, left_on = ['key1', 'key2'], right_index = True)#多层次


# In[6]:

pd.merge(lefth, righth, left_on = ['key1', 'key2'], right_index = True, how = 'outer')


# In[8]:

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
left2


# In[9]:

right2


# In[11]:

pd.merge(left2, right2, left_index= True, right_index= True, how= 'outer')#用index进行merge


# In[12]:

left2.join(right2, how = 'outer')#join也可以跟right的一个列连接 为on = 列名


# In[13]:

another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
left2.join([right2, another])


# In[14]:

left2.join([right2, another], how = 'outer')#可以join多个表


# In[15]:

arr = np.arange(12).reshape((3,4))


# In[16]:

arr


# In[17]:

np.concatenate([arr,arr], axis = 1)#numpy中根据不同轴向进行连接


# In[18]:

np.concatenate([arr,arr])


# In[20]:

#concat
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
pd.concat([s1, s2, s3])


# In[21]:

#默认concat在axis=0上工作 即union all
pd.concat([s1, s2, s3],axis = 1)


# In[22]:

s4 = pd.concat([s1 * 5, s3])
s4


# In[23]:

pd.concat([s1, s4], axis=1)


# In[24]:

pd.concat([s1, s4], axis=0)


# In[25]:

pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])#你可以通过join_axes指定要在其他轴上使用的索引


# In[27]:

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])#参与连接的片段在结果中区分不开。假设你想要在连接轴上创建一个层次化
#索引。使用keys参数即可达到这个目的
result


# In[28]:

result.unstack()


# In[29]:

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns= ['three', 'four'])
df1


# In[30]:

df2


# In[31]:

pd.concat([df1, df2])#y向连接，因为列名不一样所以加成4列


# In[32]:

pd.concat([df1, df2], axis =1, keys = ['level1', 'level2'])#x向连接 因为索引值一致 所以行数不增加


# In[33]:

pd.concat({'level1': df1, 'level2': df2}, axis=1)#另一种用字典的方法


# In[34]:

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower'])#给column取名字


# In[35]:

df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
df1


# In[36]:

df2


# In[37]:

pd.concat([df1, df2])


# In[38]:

pd.concat([df1, df2], ignore_index=True)#可以把旧的index舍弃掉  生成一个不重复的index


# In[40]:

#np.where(x>1,x,0) 检查x 如果大于1就还是x，如果小于1就弄成0
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
a


# In[41]:

b


# In[42]:

np.where(pd.isnull(a), b, a)#前面是个boolean 后面是对应的返回值


# In[43]:

b[:-2].combine_first(a[2:])


# In[44]:

a.combine_first(b)#a的nan用对应的b来填


# In[45]:

#有许多用于重新排列表格型数据的基础运算。这些函数也称作重塑（reshape）或轴向旋转（pivot）运算。
#·stack：将数据的列“旋转”为行。
#·unstack：将数据的行“旋转”为列。
#data.drop_duplicates(['k1', 'k2'], take_last=True) 对data中的k1 and k2列中的重复值进行drop 保留重复的最后项 默认保留首相


# In[46]:

#利用函数或映射进行数据转换
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})


# In[47]:

data


# In[57]:

meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':'salmon'}


# In[58]:

data['animal']= data['food'].map(str.lower).map(meat_to_animal)#food列有大写的 先转换为小写 之后匹配


# In[59]:

data


# In[60]:

data['food'].map(lambda x: meat_to_animal[x.lower()])


# In[ ]:



