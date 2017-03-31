def view(file, n)
	print('\n文件%s的前%s的内容如下:\n' %(file, n))
	f = open(file)
	for i in range(int(len(n))):
		print(f.readlines(), end = '')
	f.close
file= input(r'请输入要打开的文件(C:\\test.txt):')
n= input('Please enter the line you want to view')
view(file, n)