
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series


# In[2]:

data = DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
data


# In[3]:

data.index.map(str.upper)#给index的每一项apply上str.upper


# In[5]:

data.index = data.index.map(str.upper)# 赋值给index


# In[6]:

data


# In[7]:

data.rename(index = str.title, columns = str.upper) #rename不改变原值 产生一个新表


# In[40]:

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)#cut功能  按bin的内容分段，检测ages在bin的哪段
cats


# In[11]:

cats.codes#每个元素对应的组


# In[24]:

get_ipython().magic('pinfo pandas.core.categorical.Categorical')


# In[16]:

pd.value_counts(cats)#查一下每组多少个


# In[25]:

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']


# In[35]:

sss=pd.cut(ages, bins, labels=group_names)


# In[38]:

pd.value_counts(sss)


# In[42]:

pd.cut(ages, 4)#如果向cut传入的是面元的数量而不是确切的面元边界，则它会根据数据的最小值和最大值计算等长面元


# In[43]:

#qcut是一个非常类似于cut的函数，它可以根据样本分位数对数据进行面元划分。根据数据的
#分布情况，cut可能无法使各个面元中含有相同数量的数据点。而qcut由于使用的是样本分位
#数，因此可以得到大小基本相等的面元：说白了就是按照个数分组， 分成个数相等的4个组
data = np.random.randn(1000)
cats = pd.qcut(data, 4)
cats


# In[45]:

pd.value_counts(cats)


# In[46]:

np.random.seed(12345)


# In[49]:

data = DataFrame(np.random.randn(1000,4))
data


# In[48]:

data.describe()


# In[50]:

col = data[3]
col[np.abs(col)>3]#假设你想要找出某列中绝对值大小超过3的值


# In[ ]:



