
# coding: utf-8

# In[3]:

from pandas_datareader import data as web
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame


# In[14]:

all_data = {}
for ticker in ['AAPL','IBM','MSFT','GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000','1/11/2010')
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.items()})


# In[18]:

returns = price.pct_change()


# In[20]:

returns.tail()


# In[22]:

#Series的corr方法用于计算两个Series中重叠的、非NA的、按索引对齐的值的相关系数。与此类似，cov用于计算协方差
returns.MSFT.corr(returns.IBM)


# In[23]:

returns.MSFT.cov(returns.IBM)


# In[24]:

returns.corr()


# In[25]:

returns.cov()


# In[27]:

returns.corrwith(returns.IBM)


# In[28]:

#传入一个DataFrame则会计算按列名配对的相关系数。这里，我计算百分比变化与成交量的相关系数
returns.corrwith(volume)


# In[4]:

#获得唯一值
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
s=obj.unique()
s


# In[18]:

np.sort(s)#对array进行排序


# In[20]:

obj


# In[21]:

obj.value_counts() #检查一个series中每个值出现的次数,返回一个series 索引为唯一值 其值为频率 按计数值降序排列


# In[23]:

pd.value_counts(obj.values, sort = False) #为了便于查看，结果Series是按值频率降序排列的。value_counts还是一个顶级pandas方法，可用于任何数组或序列


# In[25]:

mask = obj.isin(['b','c'])#isin series各值是否包含于传入的值序列中的布尔型数组
mask


# In[26]:

obj[mask] #显示出带有想要的值的series


# In[29]:

data = DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4,4]})
data


# In[41]:

result = data.apply(pd.value_counts)#把数数的func执行到frame中  


# In[42]:

result #value-'1'在Qu1中出现一次 在Qu2中出现一次 在Qu3中出现一次， value-'2'在Qu1中木出现过


# In[43]:

string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data


# In[44]:

string_data.isnull()


# In[46]:

'''
dropna 根据个标签的值中是否存在缺失数据对轴标签进行过滤，可通过与之调节对缺失值的容忍度
fillna 用指定值或插值方法（ffill， bfill）填充缺失数据
isnull
notnull
'''
result = data.apply(pd.value_counts).fillna(0)
result


# In[ ]:



