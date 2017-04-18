
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame


# In[2]:

get_ipython().system('cat ch06/ex1.cvs')


# In[7]:

df = pd.read_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex1.csv')
df


# In[24]:

pd.read_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex2.csv', header = None)#列名 none的时候默认 1234


# In[25]:

pd.read_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex2.csv', names = ['a','b','c','d','message'])#names为列名


# In[28]:

names = ['a','b','c','d','message']
pd.read_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex2.csv', names = names, index_col = 'message')


# In[31]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex2.csv',names = names, sep = ',',index_col = 'message')


# In[39]:

s=open (r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\csv_mindex.csv')
print(s)


# In[40]:

list(s)


# In[44]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\csv_mindex.csv', sep = ',', index_col=['key1','key2'])


# In[45]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\csv_mindex.csv', sep = ',',header = None)


# In[50]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\csv_mindex.csv', sep = ',', index_col= 'key1')


# In[52]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex3.txt', sep='\s+')


# In[53]:

list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex3.txt'))


# In[54]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex3.txt', sep = '\s+', )


# In[56]:

list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex4.csv'))


# In[57]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex4.csv', sep = ',', skiprows=[0,2,3])


# In[58]:

list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex5.csv'))


# In[75]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex5.csv', sep = ',', na_values=0)


# In[76]:

'''
path 文件系统位置
sep or delimiter
header 用作列名的行号 默认0 如果没有应该写None
index——col
names 列名
skiprows
na_values 替换NA的值
parse_dates 尝试将数据解析为日期，默认为False，如果为True， 则尝试解析所有列，此外还可以指定需要解析的一组列号或别名。
            如果列表的元素为列表或元祖，就会将多个列组合到一起再进行日期解析工作（例如日期/时间分别位于两个列中）
comment 注释信息符号
keep_date_col 如果连接多列解析日期，则保持参与连接的列。默认为False
converters 有列名/列号跟函数之间的映射关系组成的字典。如{'foo':f}会对foo列的所有制应用函数f
dayfirst 当解析尤其以的日期是，将其看作国际格式如 7/6/2012-->June 7，2012 默认False
date_parser 用于解析日期的函数
nrows 需要读取的行数（从文件开始出算起）
iterator 返回一个TextParser 以便逐块读取文件
chunksize 文件块的大小（用于迭代）
skio_fiiter 需要忽略的行数（从文件末尾处算起）
verbose 打印各种解析器输出信息 如“非数值列中缺失值的数量”
encoding 用于unicode的文本编码格式。如“utf-8”
squeeze 如果数据经解析后仅含一列，则返回Series
thousands 千分位分隔符 如“，” or “.”
'''


# In[79]:

result = pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex6.csv', sep=',', nrows = 10)#只读10列


# In[80]:

result


# In[81]:

chunker = pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex6.csv', sep=',', chunksize = 1000)


# In[88]:

chunker = pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex6.csv', sep=',', chunksize = 1000)
tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending = False)
tot


# In[89]:

data = pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex5.csv', sep = ',')


# In[90]:

data.to_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\out1.csv')#保存成一个csv文件


# In[91]:

list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\out1.csv'))


# In[105]:

data.to_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout', na_rep= 'NULL', sep = '|' )
#可以定义分隔符,替换空值为NULL
list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout'))


# In[106]:

data.to_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout', index = False, header =False)
list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout'))


# In[108]:

data.to_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout',index = False, columns= ['a','b','c']) 
#只显示一部分列
list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout'))


# In[111]:

dates = pd.date_range('1/1/2001', periods = 7)
ts = Series(np.arange(7), index = dates)
ts


# In[112]:

ts.to_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout')
list(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout'))


# In[121]:

pd.read_table(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout', sep = ',', header= None,index = column1)


# In[122]:

Series.from_csv(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\abd.stdout', parse_dates = True)


# In[124]:

import csv


# In[127]:

f = open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex7.csv')
reader =csv.reader(f)
for line in reader:
         print (line)
         


# In[132]:

lines = list(csv.reader(open(r'C:\Users\Han Jiang\Desktop\pydata-book-master\ch06\ex7.csv')))


# In[140]:

header,values=lines[0], line[1:]


# In[141]:

data_dict={h:v for h, v in zip(header,zip(*values))}


# In[142]:

data_dict


# In[ ]:



