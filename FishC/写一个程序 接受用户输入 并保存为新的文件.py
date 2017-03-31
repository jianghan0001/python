def file_write(file_name):
	f= open(file_name)
	print('请输入内容，【单独输入':w' 保存退出')
	
	while True:
		write_some = input()
		if write_some != ':w':
			f.write('%s\n' %write_some)
		else:
			break
	f.close
file_name=input('please enter fileName!')
file_write(file_name)






def abc(fileName):
	fileName= input('please enter fileName!')
	openFile=open(fileName, 'w')
	openFile.write(input(请输入内容，【单独输入':w' 保存退出】))
	