
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import matplotlib.pyplot as plt


# In[8]:

#01training的一个练习 dow
OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
VOLUME = 4
ADJ_CLOSE =5
dow = np.loadtxt(r"C:\Users\Han Jiang\Desktop\Numpy\dow_selection\dow.csv", delimiter=",")
HV_mask = dow[:, 4] > 5.5e9
HV_mask


# In[15]:

HV_index = np.where(HV_mask)[0]
HV_index


# In[21]:

plt.plot(dow[:, 5], 'b-')


# In[22]:

plt.plot(HV_index, dow[HV_index, 5], 'ro')


# In[23]:

plt.show()


# In[24]:

'''
基本数组统计方法
sum
mean 算数平均数
std, var
min, max
argmin, argmax 最小和最大元素的索引
cumsum 所有元素累积和
cumprod 所有元素累积积
'''


# In[25]:

#any and all  any to check whether a True in a arrar, all to check whether all of them are True in a array
HV_mask.any()


# In[26]:

HV_mask.all()


# In[33]:

#排序 sort
arr= np.random.randn(8)
arr


# In[35]:

arr.sort()
arr


# In[39]:

#多维排序  给定一个轴
arr= np.random.randn(5,3)
arr


# In[44]:

arr.sort()
arr


# In[43]:




# In[47]:

#用排序选取特定位置的数字
arr= np.random.randn(1000)
arr.sort()
arr[int(0.05 * len(arr))]#第5%位数是啥


# In[49]:

# np.unique 找出数组中的唯一值并返回排了序的数组
names = np.array(['a', 'b', 'd', 'c', 'a'])
np.unique(names)


# In[50]:

# np.in1d 用于测试一个数组中的值在另一个数组中的成员资格 返回T or F
values = np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])


# In[51]:

'''
unique(x) 唯一 排序
intersect1d(x,y) 公共元素 排序
union1d(x,y) 并集 排序
in1d(x, y)
setdiff1d(x, y) 集合的差 即在x中不在y中
setxor1d(x, y) 对称差 去掉既在x也在y中的值
'''


# In[52]:

'''
读取和存储
arr = np.arange(10)
np.save('some_array', arr) 没有后缀 自动存为.npy
np.load('some_array.npy) 就把上面的array load进来了
np.savez('array_archive.npz', a= arr, b = arr)#打包存储
arch = np.load('array_archive.npz')
arch['b']    -->array([0,1,2,3,4,5,6,7,8,9])
'''


# In[53]:

x= np.array([[1,2,3],[4,5,6]])
y=np.array([[6.,23.],[-1,7],[8,9]])


# In[59]:

np.dot(x,y)


# In[55]:

x


# In[56]:

y


# In[60]:

'''
np.random 函数
seed 确定随机数生成器的种子
permutation 返回一个序列的随机排列或返回一个随机排列的范围
shuffle 对 一个序列就地随机排列
rand 产生均匀分布的样本值
randint 从给定的上下限范围内随机选取整数
randn 产生正态分布的样本值（平均值为0，标准差为1）
binomial 产生二项分布的样本值
normal 产生正态分布的样本值
beta 产生beta分布的样本值
chisquare 卡方分布
gamma gamma分布
uniform 产生在【0，1）中均匀分布的样本值
'''


# In[80]:

#随机走1000步 看看是咋走的
nsteps = 1000
draws = np.random.randint(0,2,size = nsteps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum()
walk


# In[87]:

plt.plot(walk)


# In[88]:

plt.show()


# In[97]:

np.random.choice(100, 3)


# In[98]:

#第一个大于10的点
(np.abs(walk)>=10).argmax()


# In[ ]:



