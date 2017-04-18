
# coding: utf-8

# In[54]:

import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame


# In[2]:

obj = """{"name": "Wes", "places_lived": ["United States", "Spain", "Germany"], "pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"}, {"name": "Katie", "age": 33, "pet":
"Cisco"}]}"""


# In[3]:

import json


# In[5]:

result = json.loads(obj)#json 转换为python格式
result


# In[7]:

asjson = json.dumps(result)#又给弄回json
asjson


# In[8]:

siblings = DataFrame(json.loads(obj)['siblings'], columns = ['name', 'age'])
siblings


# In[3]:

from lxml.html import parse
from urllib.request import urlopen


# In[5]:

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))


# In[6]:

doc = parsed.getroot()


# In[7]:

links = doc.findall('.//a')
links


# In[8]:

lnk= links[28]


# In[9]:

lnk


# In[11]:

lnk.get('href')


# In[12]:

lnk.text_content()


# In[13]:

urls = [lnk.get('href') for lnk in doc.findall('.//a')]


# In[14]:

urls[-10:]


# In[16]:

tables = doc.findall('.//table')
tables


# In[17]:

from pandas.io.parsers import TextParser


# In[18]:

def parse_options_data(table): 
    rows =table.findall('.//tr') 
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()


# In[19]:

call_data = parse_options_data(calls)
put_data = parse_options_data(puts)
call_data[:10]


# In[20]:

import requests


# In[21]:

url= 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
resp


# In[22]:

import json


# In[23]:

data = json.loads(resp.text)


# In[25]:

data.keys()


# In[28]:

#读取Microsoft Excel文件
#ExcelFile用到了xlrd和openpyxl包
#路径即可创建一个ExcelFile实例：
xls_file = pd.ExcelFile('data.xls')
#存放在某个工作表中的数据可以通过parse读取到DataFrame中：
table = xls_file.parse('Sheet1')


# In[29]:

import sqlite3
query = """CREATE TABLE test(a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()


# In[41]:

data = [('Atlanta', 'Georgia', 1.25, 6), ('Tallahassee', 'Florida', 2.6, 3), ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
test


# In[39]:

import pandas.io.sql as sql
sql.read_sql('select * from test',con)


# In[42]:

#数据分析和建模方面的大量编程工作都是用在数据准备上的：加载、清理、转换以及重塑
#数据集的合并（merge）或连接（join）运算是通过一个或多个键将行链接起来的。这些运算
#是关系型数据库的核心。pandas的merge函数是对数据应用这些算法的主要切入点。
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
df1


# In[43]:

df2


# In[44]:

pd.merge(df1, df2, on = 'key')#妈的 就是inner join 


# In[45]:

pd.merge(df1, df2, how = 'outer')


# In[46]:

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 =DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')#如果两个对象的列名不同，也可以分别进行指定：


# In[48]:

pd.merge(df1, df2, on = 'key',suffixes = ('_df1','_df2'))


# In[49]:

left = DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')


# In[50]:

pd.merge(left, right, on='key1')


# In[56]:

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))#出去merge主键 其他相同的键给予不同后缀


# In[65]:

left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]},index=['a', 'b'])


# In[62]:

left1


# In[64]:

right1


# In[69]:

pd.merge(left1, right1,  left_on='key', right_index=True) #保留right_index


# In[ ]:



