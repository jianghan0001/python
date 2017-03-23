# replace a letter in a word
s= 'hello'
s= 'y'+s[1:]
#now s should be yello

s= 'abcdef'
s[::-1] #s should be fedcba  so here -1 means reverse
s[-1] #s should be f
s[2:5] #def start at 0 end before 5(not include 5)

i=0
word=input('please give me a word')
for i in range(len(word)):
	print(word[i])
	i=i+1
	
i=0
word=input('please give me a word')
while i < len(word):
	print(word[i])
	i=i+1
	
#bisection method to find square root
x=25
high=x
low=0.0
ans=(high+low)/2.0
epsilon=0.01
while abs(ans**2-x)>epsilon:
	if ans**2 < x:
		low= ans
	else:
		high=ans
	ans=(low + high)/2.0
print(ans)


#guess a number by bisection
print('think a number')
high=100
low=0
da=False
while not da:
    ans=(high + low)//2
    jin=input('%d is c or h or l' %ans)
    if jin=='c':
        print('oh yeah!')
        da=True
    elif jin=='h':
        high= ans
    elif jin== 'l':
        low= ans
    else:
        print('gundan')
print('Your number is %d' %ans)

#Newton-Raphson 猜平方根 g=g-(g**2-k)/(2*g)
epsilon=0.01
num=54.0
guess=num/2.0
while abs(guess**2-num)>epsilon:
	guess=guess-(((guess**2)-num)/(2*guess))
print ('Square root of '+ str(num) +'is about '+ str(guess))

#string method
str1 = 'exterminate!' 
str2 = 'number one - the larch'

str1.upper()  
'EXTERMINATE!'

str1.isupper()
False

str1.islower()
True

str2 = str2.capitalize()
str2
'Number one - the larch

r2.swapcase()
'nUMBER ONE - THE LARCH'

str1.index('e')
0

str2.index('n')
8

str2.find('n')
8

str2.find('!')
-1

str1.count('e')
3

str1 = str1.replace('e', '*') 
str1
'*xt*rminat*!'

str2.replace('one', 'seven')
'Number seven - the larch'

#a的b次方 两种方法
def iterPower(a,b):
ans=1
while b>0:
	ans*=a
	b-=1
return ans

def recurPower(a,b):
	if b==0:
		return 1
	else:
		return a* recurPower(a.b-1)

# Hanoi tower

def printMove(fr, to):
    print('move from ' + str(fr) +  ' to ' + str(to))
def towers(n, fr, to, spare):
    if n==1:
        printMove(fr,to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
print(towers(5,'p1','p2','p3'))

#找出a,b 2个数的最大的共同整除数
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)
	# set testValue起始点为a and b 中小的那个
    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
	#or 只要有一个为真则为真 当a and b都能被一个testValue整除时循环才停止
        testValue -= 1
		#每个循环testValue-1,因为1可以被所有数整除 所以到1就停止 输入负数会无限循环
        print('a')

    return testValue

print(gcdIter(10,15))
"""
Write a procedure called oddTuples, which takes a tuple as
 input, and returns a new tuple as output, where every 
 other element of the input tuple is copied, starting
 with the first one. So if test is the tuple
 ('I', 'am', 'a', 'test', 'tuple'), then evaluating
 oddTuples on this input would return the tuple 
 ('I', 'a', 'tuple').
def oddTuples(aTup): 
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    rTup= () #创建一个占位符
    index=0
    while index< len(aTup):
        rTup=rTup+(aTup[index],)
        index+=2 #隔一个塞一个
    return rTup
# list function
L=[2,1,3]
L.append(5)# L should be [2,1,3,5]
L1=[4,5,6]
L2= L+ L1 #L2 should be[2,1,3,5,4,5,6]
L.extend([0,6])#[2,1,3,5,0,6]
del(L[0])#[1,3,5,0,6]
L.pop() #return the last part
L.pop(1)# 位置1--》3
L.remove(3) #[1,5,0,6]

s='abc'
List(s) #['a', 'b', 'c']
s.split() #括号内为以神马为分界点 分界点会被去掉，形成一个list []
''.join(b)#把b list里面的内容全部join起来 无空
'_'.join(b)#用下划线join起来
sorted(L) #return sorted L but not change L1
L.sort() #change L ASC
L.reverse()#reverse order of the list
L.index(1)# should be 1  1 in the parameter is 内容 不是序号 返回的是它在list里面的位置
L2=L1#复制L1 when anything changed in L1, L2 will also be changed, L2 either
L2=L1[:]#复制一份L1给L2 L2是一个独立的 不会随着L1 改变

def remove_dups(L1,L2):
	for e in L1:	
		if e in L2:
			L1.remove(e)
L1=[1,2,3,4,5，6]
L2=[3,4,5,6]
remove_dups(L1,L2)
#will only remove 3 因为删掉3之后 L1就变了  4的位置变成3了 导致4删不掉 但5能删掉 6同4
#删除前先复制一个新表 然后让e在新表中 这样就不会影响旧表的删除
def remove_dups(L1,L2):
	Copy_L1=L1[:]
	for e in Copy_L1:	
		if e in L2:
			L1.remove(e)
L1=[1,2,3,4,5，6]
L2=[3,4,5,6]
remove_dups(L1,L2)

#function in function f is a function
def applyToEach(L, f):
	for i in range(len(L)):
		L[i]=f(L[i]) #L list的每一项都要被f function 处理一下
L=[1, -2, 3.4]
applyToEach(L, abs)#[1, 2, 3.4]
applyToEach(L, int)	#[1, 2, 3]
applyToEach(L, fact)#[1, 2, 6]
applyToEach(L, fib) #[1, 2, 13] 

#list of function
def applyFuns(L, x):
	for f in L:
		print(f(x))
applyFuns([abs, int, fact, fib], 4)
#map(function, [list]) --map function 把function apply到list里面的每一项
for i in map(abs,[-1, -2, 3, 4])# i is [1,2,3,4]
#do compare for 2 list
L1=[1, 4, 5, 9]
L2=[3, 1, 2, 11]
for i in map(min, L1, L2): #i should be [1,1,2,9]
#让list里的每个值乘以5  先定义个乘以5的function 之后套进去
def timesFive(a):
    return a * 5
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
testList = [1, -4, 8, -9]
applyToEach(testList, timesFive)
#
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
applyEachTo([inc, square, halve, abs], -3)#[-2, 9, -1.5, 3]

 #dictionary 
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}
animals # {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}
animals['c']#'coati'
animals['donkey']#Error 只能用key找value
len(animals)#4
animals['a'] = 'anteater'#把a改成anteater
len(animals['a'])#8 用key a调出anteater
'baboon' in animals #False
'donkey' in animals.values()# True  .value() 列出所有value
'b' in animals#True
animals.keys() #列出所有key ['a', 'b', 'c', 'd']
del animals['b']#删掉b那行
animals.values() #前缀是必须的 dict_values(['anteater', 'coati', 'donkey'])
#using dictionary
#1 create dictionary from a song a word with 出现次数
def lyrics_to_drequencies(lyrics):#此fun为数一个list里面每个东西出现的次数 创建dict如{'a':3, 'b':4...}
	myDict={}#创建一个空洞dict先
	for word in lyrics: #word as key and 出现次数 as value
		if word in lyrics: #lyrics是一个list
		myDict[word]+= 1 #myDict[word]是key 会返回对应的value 即出现次数
		else:
			myDict[word]=1
	return myDict
#2 find the most common words
beatles= lyrics_to_drequencies(song_name)
def most_common_words(freqs): #freqs就是个占位符 代表一个dict
	values=myDict.value()#make a list of values
	best= max(values) #find the max value
	words=[]
	for k in fregs:
		if freqs[k]== best:
			words.append(k)
	return(words, best)
(w, b)= most_common_words(beatles)
w#list of the word
b#number of the most common
#3 del 出现5次以上的
def words_offen(freqs, minTimes):
	result=[] #set up an ampty list initially 
	done= False#flag  
	while not done: #as long as we have something to do, do it
		temp=most_common_words(fregs)
			if temp[1]>= minTimes:#temp[1]是上个功能里面做出来的d list 里面有出现的次数 temp是[['a', 'b', 'c'], [4]]这种结构
				result=result.append(temp)
				for w in temp[0]:# 指上个功能做出来的words w list
					del (freqs[w])#删掉key 即整行删除 freqs是个dict 
			else:
				done= True
	return result #result表示删掉的东西
	
	# 给个dict 找里面的list的个数最多的
	def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
		result = None
		biggestValue = 0
		for key in aDict.keys():
			if len(aDict[key]) >= biggestValue:
				result = key
				biggestValue = len(aDict[key])
		return result
#use dict store result already got 来加速
def fib(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	else:
		fib(n)=fib(n-1) + fib(n-2)
#楼上的当数变大的时候会慢 因为fib在反复的算 如果把算过的fib存起来 会加快

def fib_efficient(n, d):
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
		d[n] = ans
		return ans
d = {1:1, 2:2}
print(fib_efficient(3, d))

#except assert
while True: #只有给了数的才会到达gundan  否则一直循环while True
    try:
        n=input('lai ge shu')
        n=int(n)
        break
    except: #有错就执行这里
        print('shabi')
print("gunba")

# 打开一个文件 把它split掉  然后在新list里分下组
data=[]
file_name=input('provide a name of a file of data')
try:
    pi=open(file_name, 'r')
except:
    print('cannot open [0]'.format(file_name))
else:
    for new in pi:
        if new != '/n':
            addIt= new[:-1].split(',')#remove trailing \n
            data.append(addIt)
finally:
    pi.close() #close file even if fail
gradeData=[]
if data:
    for student in data:
        try:
            name=student[:-1]
            grades= int(student[-1])
            gradeData.append(name, grades)
        except:
            gradeData.append([student[:], []])

#except could be a condition when reach it appear
def get_ratios(L1, L2):
    ratios=[]
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = not a num when ZeroDivisionError appear it will replace wrong value with nan
        except:
            raise ValueError ('get_ratios called with bad arg ')
    return ratios
L1=[1,2,3]
L2=[4,5,6]
L3=[[1,2],3,4]
L4=[0,3,4]
L5=[a,1,1]
L6=[L1, L2, L5]
print(get_ratios(L1,L2))#OK
print(get_ratios(L1,L4))#0--nan
print(get_ratios(L1,L6))#L3 and L6 all typeerror
print(get_ratios(L1,L5))#get_ratios called with bad arg
#except create new-grade
def get_stats(class_list):
	new_stats=[]
	for lte in class_list:
		new_stats.append([lte[0], lte[1], avg(lte[1])])
	return new_stats
def avg(grades):
    try:
	    return sum(grades)/len(grades)
    except ZeroDivisionError:
        return 0.0
test_grade=[[['peter','parker'],[10.0, 5.0, 85.0]],
			[['bruce', 'wayne'], [10.0, 8.0, 74.0]],
			[['captain', 'america'], [8.0, 10.0, 74.0]],
			[['deadpool'], []]]
print(get_stats(test_grade))
#[[['peter', 'parker'], [10.0, 5.0, 85.0], 33.333333333333336], [['bruce', 'wayne'], [10.0, 8.0, 74.0], 30.666666666666668], [['captain', 'america'], [8.0, 10.0, 74.0], 30.666666666666668], [['deadpool'], [], 0.0]]		
		
#小甲鱼

import random
secret = random.randint(1, 10)  # 生成一个1-10的随机数赋给secret
print('-----------I love Chelsea-----------')
da = False
while not da:
    try:
        temp = input('please input a number between 1-10: ')
        guess = int(temp)
        if guess == secret:
            print('{0} is the number, bang!'.format(guess))
            da = True
        elif guess > secret:
            print('da le da le')
        else:
            print('xiao le xiao le')
    except:
        print('num num num')
print('game over')

		
#在python中只有以下情况被看作假，注意连空格都不能有--False, None, 0, (), [], {}, '', ""  
#以一个循环作为条件 打印另一个循环
temp = input('请输入一个整数:')
number = int(temp)
i = 1 
while number:
    print(i)
    i = i + 1
    number = number - 1	
'''
1
2
3
4
5
6
7
8
'''	
#循环套循环 循环里面第一个循环走完 再走第二个循环 里面2个循环走完再走外面大循环 都走完才结束 end="" 表示不换行 继续在这一行 print命令默认换行
temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print(' ', end = '')#end = '' 表示不换行 连着来 ' '加个空格就用空格隔开
        i = i - 1
    j = number
    while j:
        print('*', end = '')
        j = j - 1
    print()
    number = number - 1
'''
请输入一个整数:8
       ********
      *******
     ******
    *****
   ****
  ***
 **
*

'''	
type(a)#返回a的数据类型
isinstance(a, b)# a是变量 b是数据类型--int/str 此功能返回True or False 即判定a,b的数据类型是否相同
isdigit()
is_integer()
assert #断言 当这个关键词后的条件为假的时候 程序崩溃 自爆		
small = x if x < y else y 
#有红蓝绿3种球 其中红3 蓝3 绿6 混合后从中任意拿8个 球组合
print('red\tblue\tgreen')
for red in range(0, 4):
	for blue in range(0, 4):
		for green in range(2, 7):#注意 因为总数是8个 所以绿的不能小于2
			if red + blue + green == 8:
				print (red, '\t', blue, '\t', green)
		
		
#用户有三次输入密码的机会 如果输入的有'*' 则不算 重新输入
password = 'wwwwwww'
count = 3
while count:
    pwd = input('please enter you password.')
    if pwd == password:
        print ('wo cao ni dui le!')
        count = 0
    elif '*' in pwd:
        print('you should not use * in you password')
        continue
    elif pwd != password:
        count -=1
        print('zai lai yici, you have {0} times left'.format(count))
print('gun dan ba ni')	
abc=[1,2,3]
abc.append(只能是一项)
abc.extend(可以是列表)	
abc.insert(位置，内容)	
abc.remove('删除内容')
del abc[index number]
del abc#整表删除
abc.pop()#返回最后一项并删除
name=abc.pop()#可以赋值
name=abc.pop(index number)	
abc[1:3]#列出1项和2项
list 比较只比较第一个值 返回T or F
dir(list) #显示出有关list的所用函数
abc.count(内容)#数内容次数
abc.index(内容)
abc.index(内容，2，4#范围)
abc.reverse()
abc.sort()#改变顺序
abc.sort(reverse=True)#逆序

# iphython notebook
# linux 装软件 简单 pip install jupyter
# pip install numpy
# pip install padas
# Anaconda 是个包裹 啥都有
# cmd里面输入ipython就可以进入ipython界面
# cmd 输入 Jupyter notebook就能进入IE 界面
# 名字后面输入？ 显示这个名字的属性 data?
# np.*load*? np里有关load的函数
# import numpy as np 调用numpy包裹 
# data= {i: np.randam.randn() for i in range(7)}
# shift + enter 执行
# 打几个字按tab for auto-completion
# %run 文件名.后缀  在一个文件中run另一个文件
# import matplotlib.pyplot as plt
# %matplotlib inline
# np.random.randn(50).cumsum() 弄50个随机数然后累加
# plt.plot(np.random.randn(50).cumsum()) 用plt功能绘图
# abc=!dir 跟系统交互 执行系统命令 ‘！’表示执行
# %pwd %hist显示历史
# run 文件  for debug  一行一行执行
[i*i for i in range(10)]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#list comprehensions 列表解析
#[有关A的表达式for A in range(B)] 
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]] 
#字符串方法
str1.capitalize()#首字母大写 不改变原str1
str1.casefold()#所有改小写 不改变原str1
center(width)#居中
count(sub, sta, end)
	
		
		