
# coding: utf-8

# In[2]:

import pandas as pd
from pandas import Series, DataFrame 
import numpy as np
pop ={'NV':{2001:2.4, 2002:2.9}, 'OH':{2001:1.1, 2002:3.1}}


# In[3]:

frame3 = DataFrame(pop)
frame3 #嵌套字典的dataframe 以外层字典key为列，内层字典key为index 成表


# In[4]:

frame3.T #转置


# In[6]:

frame3.values


# In[7]:

obj = Series(range(3), index= ['a','b','c'])


# In[8]:

index = obj.index


# In[9]:

index


# In[10]:

index[:2]


# In[11]:

frame3


# In[12]:

'OH' in frame3.columns


# In[13]:

2001 in frame3.index


# In[14]:

obj = Series([4,22,1,44], index= ['d','b','a','c'])
obj


# In[16]:

obj2= obj.reindex(['a','b','c','d','e','f'])
obj2


# In[17]:

obj2= obj.reindex(['a','b','c','d','e','f'], fill_value=33)
obj2


# In[21]:

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3


# In[19]:

obj3.reindex(range(6), method='ffill') #ffill向forward填充


# In[22]:

obj3.reindex(range(6), method='bfill') #向back填充


# In[27]:

frame = DataFrame (np.arange(1,10).reshape((3,3)), index = ['a','c','b'], columns = ['OH','CA','PA'])
frame


# In[33]:

frame2 = frame.reindex(index= ['a','b','c','d'], fill_value =11)
frame2


# In[ ]:



