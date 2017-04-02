#else 更牛逼
#和while and for合用


try:
	int('abc')
except: ValueError as reason:
	print('出错了：'+str(reason))
else:#没错就执行else
	print('没有任何异常')
	
#with
try:
	with open('data.txt', 'w') as f:#这里有with就不用最后面的finally 会自动关闭
		for each_line in f:
			print(each_line)
except OSError as reason:
	print('出错啦' +str(reason))
finally:
	f.close()