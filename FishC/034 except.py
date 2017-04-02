#exception
try:
	f-open('我为什么是一个文件.txt')
	print(f.read())
	f.close()
except OSError as reason:
	print('文件出错了\n错误原因是'+ str(reason))
except TypeError as reason:
	print('类型出错了\n错误原因是'+ str(reason))
except:#不管错误类型 不推荐
	print('出错啦')
#try语句一旦出现异常，后面的不会继续
finally:
	这里的东西不管怎么样都会被执行，通常是关闭文件
raise#一个异常 ZeroDivisionError

if 'f' in local():#如果f这个变量存在当前局部变量符号表的话
	f.close()