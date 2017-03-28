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
str1.center(width)#居中
str1.count(sub, sta, end) #范围可写可不写
str1.endswith(内容)  # T or F/startswith()
str1.find(neirong)#返回索引值 没有的话返回-1
index(neirong)# 返回索引值 没有的话返回异常
isalnum()#如果字符串中至少有一个字符 且全为字符和数字 返回T 反之F
isalpha()#只有字符
isdecimal()#只有10进制
isdigit()#只有数字
islower()#
isnumeric()#只有数字
isspace()#只有空格
istitle()#只有且全部首字母大写
isupper()#大写
join(内容)# str1='ab' str2='12345' str2.join(str1) should be a12345b12345
ljust()#左对齐
lower()#转小写/upper()
lstrip()#去掉左边所有空格/ rstrip()/strip() 只对2边的东西有效
partition(neirong)# str2.partition(3) should be('12', '3', '45')
replace(old, new, [count])
split()#切分 啥也不放 默认空格 切啥啥消失
swapcase()#大小写互换
title()#返回标题式 每个词大写开头
#在字符串前加‘r’表示使用原始字符串 file1 = open(r'C:\windows\temp\readme.txt', 'r')
'{0:.1f}{1}'.format(27.658, 'GB') #'27.7GB'
'{0}{1:.2f}'.format('Pi = ', 3.1415)#'Pi = 3.14'
'%c %c %c' %(97, 98, 99) #'a b c' ASCII码   
%s #字符串
%d #格式化整数
%o #8进制 '%o' %10 # 12
%x # '%x' %10 #a
%X # '%X' %10 #A '%X' %160 #A10
%f #定点数 '%f' %27.658 # 27.658000 默认8位
%e # 科学计数法 '%e' %27.658 # 2.765800e+01
%g #只能版本 根据大小自动选择%f or %e
m.n n指小数点后面位数 m基本打酱油 %.2f %.2e 
%# 显示8(o)和16(x)进制 如 '%#o' %10 # 0o12  '%#X' %108 #0X6C
'%010d' %5 #'0000000005' 0表示用0占位空格 10表示定位10位

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

a = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = '0123456789'
pw=input('please enter your password')
pwl=len(pw)
while (pwl == 0) or pw.isspace():
    pw=input('please reenter your password with something!')
    pwl=len(pw)
if pwl <= 8:
    pw_l = 1
elif 8 < pwl < 16:
    pw_l = 2
else:
    pw_l = 3
flag_con = 0
pw_c = 0
for each in pw:
    if each in a:
        pw_c +=1
        break
for each in pw:
    if each in b:
        pw_c +=1
        break
for each in pw:
    if each in c:
        pw_c += 1
        break
while 1:
    print('Your password level is ', end='')
    if pw_l == 1 or pw_c == 1 :
        print('low')
    elif pw_l == 2 or pw_c == 2:
        print('medium')
    elif pw_l == 3 or pw_c == 3:
        print('high')
        print('继续保持！')
        break
    print('请按以下方式提升您的密码安全级别:\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位')
    break

a=list()#a 是个空[]
b= 'abc'
b=b.list() # ['a', 'b', 'c' ] tuple也能这么搞
sum(numbers, 8)#指求完numbers的和再加8
sorted(abc)
list(reversed(numbers))
list(enumerate(numbers))#索引值变元组第一个和值组成元组
list(zip(a, b)) #合成list a and b 成双成对打包
def abc(*param)  #*号表示N多个变量
global/nonlocal 可以改变全局变量
lambda x ：2 * x + 1 #匿名函数 左边参数 右边return内容
fileter(函数，可迭代序列 iterable）#过滤器 两个参数 第一个参数可以是个None or function，第二个可迭代数据中每个元素作为function的参数进行运算，把返回True的元素组成一个新的列表返回  
fileter(None, [1, 0, False, True])#过滤掉非True结果

def odd(x):
	return x % 2 #奇数返回1(True) 偶数返回0(False)
temp = range(10)
show = filter(odd, temp) #[1, 3, 5, 7, 9] 用odd功能对temp进行筛选 对True进行返回
list(filter(lambda x: x % 2, range(10))) #先是功能 后面是实现功能的地方

map(函数，可迭代序列 iterable) #映射 将序列的每一个元素作为函数的参数进行运算加工，返回所有元素加工完成后的新序列
list(map(lambda x : x * 2, range(10)))#[0,2,4,6,8,10,12,14,16,18]
#zip 会将2个数以元组的形式组合起来
#list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) #[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)] 
#问如何弄成list模式
list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
#[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
#列表推到式 100以内能整除3的数
[ i for i in range(1, 100) if not(i%3)]
def fun_A(x, y=3):
        return x * y
lambda x, y=3 : x * y
#上面2个一回事
#递归 汉诺塔 树结构 函数调用自身的行为 有一个结束循环的行为 递归递归要有归
#1*2*3*4*...n
def factorial(x):
	result = x
	for i in range(1, x):
		result = result * i
	return result
def r(x):
	if x == 1 :
		return 1
	else:
		return x * r(x-1)
import sys 
sys.setrecursionlimit(10000)#默认递归100层  用这个可以改
#fabnacci数列
def fab(n):
	n1 = 1
	n2 = 1
	n3 = 1
	if n < 1: 
		print('Wrong input')
		return -1
	while (n - 2) > 0:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		n -= 1
	return n3
print(fab(20))		
#递归写法
def F(n):
	if n < 1 :
		print('wrong input')
		return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)
result = F(20)
if result != -1
	print('There are total %d pair of rabbit' %result)
#汉诺塔
def hanoi(n, fr, empty, to):
	if n == 1:
		print(fo, '-->' to)
	else:
		hanoi(n-1, fr, to, empty)#将n-1个盘子移动到empty上
		print(fr, '-->', to)将最底下的最后一个盘子移动从x移动到z上
		hanoi(n-1, empty, fr, to)#将n-1个盘子移动到to上
#使用递归编写一个十进制转为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）	
def decimal_to_binary(n)
	result= ''
	if n:
		result = decimal_to_binary(n // 2)
		return result + str(n % 2)
	else:
		return result
#写一个函数 get_digit(), 将参数n分解出每个位的数字并按顺序存放到列表中 例get_digit(12345)-->[1,2,3,4,5]
result=[]
def get_digit(n):
	if n > 0:
	result.insert(0, n%10)
	return get_digit(n // 10)
#dictionary 花括号 key value
brand = ['Lining', 'Nike', 'Adidas', 'FishC']
slogan= ['一切皆有可能', 'Just do it', 'Impossible is nothing', '让变成改变世界']
dict1={'Lining': '一切皆有可能', 'Nike': 'Just do it', 'Adidas' : 'Impossible is nothing', 'FishC': '让变成改变世界'}
print('FishC工作室的口号是', dict1['FishC'])
dic2={1:'one', 2: 'two', 3: 'three'}
dict3={}#empty dict
dict4=dict((('F', 70), ('i', 105), ('s', 115),('h', 104),('C', 67)))#list也OK 那么多括号是因为dict只接收一个参数 
#{'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}
dict5= dict(小甲鱼='让编程改变世界'，苍井空='让AV征服世界')#Key不能带引号
#{'小甲鱼': '让编程改变世界', '苍井空': '让AV征服世界'}
dict5['苍井空']='所有AV从业者都要通过学习编程来提高职业技能'
#now dict5 is {'小甲鱼': '让编程改变世界', '苍井空': '所有AV从业者都要通过学习编程来提高职业技能'}
#直接通过以上方法改变value， 如果dict5 中没有这个key 就添加新的key+value
#一下代码都是在执行一个操作
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})



















	
		
		