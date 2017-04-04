
# coding: utf-8

# In[1]:

import numpy as np


# In[10]:

a= np.array([1, 2, 3, 4, 5])
b= np.array([10, 20 , 30, 40, 50])


# In[11]:

a+b


# In[12]:

a+1


# In[13]:

a*b


# In[15]:

c=np.arange(11.)
c


# In[19]:

y=np.sin(c)
y


# In[20]:

import matplotlib.pyplot as plt


# In[21]:

plt.plot(c, y)


# In[23]:

plt.show()


# In[24]:

c.dtype


# In[25]:

type(c)


# In[26]:

c.itemsize#每个元素的大小


# In[27]:

c.size#有多少个元素


# In[28]:

c.shape #一维向量5个元素


# In[29]:

#a.fill(4)#把a里面都填上4 or a[:]=4 前者更快


# In[30]:

#如果往整型的list里填浮点数 会把小数点后面都去掉
#numpy的loadtxt() load表比较高效简单


# In[31]:

#arr=np.loadtxt('path\\abc.txt')  不需要更改格式 分隔符啥的
#arr=np.loadtxt('path\\abc_withheader.txt',skiprows=1) 有head可以skiprows掉 =几就跳过第几行
#arr=np.loadtxt('path\\abc_complex.txt', skiprows = 1, dilimiter = ',', comments = '%', usecols=(1,2,3,5), dtype= int) 


# In[33]:

x= np.linspace(0, 2*np.pi, 101)#从0开始到2个pi分割101分的list
y= np.sin(x)
s= 0.5*(x[:-1]+x[1:])
t= (y[1:]-y[:-1])/(x[1:]-x[:-1])
plt.plot(s,t)
plt.show()


# In[34]:

#二维  a[0, 3:5] 第0行 的第4个和第5个（记住0开头）
# a[4:, 4:] 第5行往下，第5列往右全要[[5r5c,5r6c,5r7c,5rnc],[6r5c,6r6c,6r7c,6rnc],[nr5c, nr6c,nr7c,nrnc]] r=rows c=columns
# a[:, 2] 第3列全要[r0c3,r1c3,r2c3,rnc3]
# a[2::2,::2] 跳跳更健康 [第3行往n行跳，一次跳2步，从0列开始跳，每次2步]
# a=[(0,1,2,3,4),(1,2,3,4,5)]斜向的一个数列[r0c1,r1c2,r2c3,r3c4,r4c5]
# mask=arrar([1,0,1,0,0,1], dtype = bool) a[mask,2] means [[0,2,5], 2]


# In[35]:

#b=a[1,3]
#b[0]=15
#a[1]will be changed to 15 because b reference from a
#b=a[1,3].copy() b就实体化了  change of b will not infect a 


# In[36]:

#where  
#a=array([[0,12,5,20],[1,2,11,15]])#2rows and 4 co;umns
#loc=where (a > 10)-->返回的是个元组，里面是索引值，第一个list和第二个list配合起来是个坐标
#loc --> (array[0,0,1,1],[1,3,2,3]) 
#a[loc] --> array([12,20,11,15])


# In[1]:

#一个练习 dow
OPEN=0
HIGH=1
LOW=2
CLOSE=3
VOLIME=4
AD_CLOSE=5
dow=np.loadtxt('path\\dow.txt',delimiter = ',')
HV_mask=dow[:, VOLUME] >5.5e9 #产生[0,1,0,0,1,1,1]这样的东西
days= sum(HV_mask)
HV_index = np.where(HV_mask)[0] #赋到行上 显示出第几第几行啥的
plt.plot(dow[:, ADJ_CLOSE, 'b-'])
plt.plot(HV_index, dow[HV_index, ADJ_CLOSE], 'ro')
plt.show()


# In[3]:

#NumPy（Numerical Python的简称）
#pandas这个名字本身源自于panel data
#JSON（即JavaScript Object Notation，这是一种常用的Web数据格式）
#%timeit这个魔术命令检测任意Python语句（如矩阵乘法）的执行时间
#在IPython中，以感叹号（!）开头的命令行表示其后的所有内容需要在系统shell中执行


# In[14]:

import numpy as np
data = {i: np.random.randn() for i in range(7)}


# In[17]:

data


# In[32]:

import this


# In[29]:

a


# In[34]:

data =np.array ([[1,2,3],[10,20,30]])


# In[35]:

data


# In[40]:

data*10


# In[41]:

data + data


# In[42]:

data.shape


# In[43]:

data[1]


# In[44]:

data[0][0]


# In[45]:

data.dtype


# In[47]:

s= np.zeros(10)#创建一个全0的10位数组 类似 np.ones. np.zeros_like 以另一数组为参数 创建结构一致但全0的数组 


# In[48]:

s


# In[50]:

s=np.zeros((3, 6))#创建一个3行6列队全0数组


# In[51]:

s


# In[52]:

s= np.empty((2,3,2)) #创建一个2行3列2面对数组,因为empty 所以内部值全为垃圾


# In[53]:

s


# In[55]:

s= np.arange(10)


# In[56]:

s


# In[57]:

#asarray  将输入转换为ndarray


# In[62]:

np.eye(3,3,3)


# In[63]:

arr1 = np.array([1,2,3], dtype=np.float64) #可以在后面直接定义数据类型 这样数组的站位就变成8个字节了


# In[64]:

arr1.dtype


# In[73]:

arr2 = arr1.astype(np.int32) #用astype改变原始参数类型，注意 如果浮点数改为整数 则小数点后面的都消失
arr2.dtype


# In[74]:

arr3 = arr2.astype(arr1.dtype) #改变为另一个数组的类型
arr3.dtype


# In[79]:

arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr4[0][1] #2种方法进行索引 都可以  这种相成先找出第0行 再找这行里的第一个元素


# In[80]:

arr4[0,1]#2维定位 0行1列


# In[81]:

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names == 'Bob'#返回一个布尔型的数组


# In[89]:

data = randn(7,4)
data


# In[90]:

data[names == 'Bob']#以布尔型数组为index 显示出True的行


# In[91]:

data[names != 'Bob']#还可以用不等于喲


# In[93]:

data[names == 'Bob', 2:]#与slice合用


# In[94]:

#布尔运算符 &(and) |(or)
#将数列中小于0的都改为0
data[data<0]=0


# In[95]:

data


# In[98]:

data[names=='Bob'] = 123


# In[99]:

data


# In[102]:

data[1,2] #第1行第2列


# In[103]:

data[[1,2]] #第1行和第2行


# In[104]:

data[[2,1]]#还可以换顺序


# In[116]:

arr = np.arange(32).reshape(4,2,4)#3维度第一个数为面
arr


# In[117]:

arr. transpose(1,0,2)#3维度转换 面变成行，行变成面


# In[108]:

arr.T#行列互换  


# In[111]:

arr=np.random.randn(6,3)
np.dot(arr.T,arr)


# In[122]:

arr = np.empty((8,4), dtype = int)
for i in range(8):
    arr[i]= i
arr


# In[124]:

arr = np.arange(10)
np.sqrt(arr)#sqrt 平方根


# In[125]:

np.exp(arr)


# In[127]:

x= randn(8)
y= randn(8)
np.maximum(x,y)#对比2个数组 取最大值组成一个新数组


# In[ ]:

arr = randn(6)*5
np.modf(arr)#将小数与整数分开形成2个数组


# In[138]:

arr = np.array([1, 'a', 3])
arr
np.isnan(y)


# In[139]:

'''
abs 绝对值
sqrt 平方根 相当于arr ** 0.5
square 平方 arr ** 2
exp 计算个元素的指数e
log 自然对数
sign 计算各元素的正负号 1正 00 -1负
ceil 大于等于该数的整数
floor 小于等于该数的整数
rint 4舍5入取整数 保留dtype
modf 分成2个数组 小数和整数
isnan 返回一个表示“哪些值是NaN（这不是一个数字）"的布尔型数组 数字返回False
isfinite, isinf 判断有穷无穷 返回T/F
cos, cosh, sin, sinh, tan, tanh 双曲型三角函数
arccos, arccosh, arcsin, arcsinh, arctan, arctanh, 反三角函数
logical-not 计算个元素not x的真值 相当于-arr
二元ufucnc
add, substract, multiply, dicide, floor_divide 加减乘除，向下圆整除
power x的y次幂
maximum, fmax fmax忽略NaN
minimum， fmin
mod 求模（除法余数）
cospysign 将第二个数组中个元素的符号复制给第一个数组
'''


# In[145]:

x=3^10
x


# In[146]:

arr = randn(4,4)
arr


# In[147]:

np.where(arr>0,2,arr)#如果大于0替换其值为2，否则保留原值


# In[149]:

np.where(arr>0,2,-1) #大于0替换成2否则替换成-1


# In[ ]:



