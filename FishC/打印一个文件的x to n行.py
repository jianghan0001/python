def file_view(file_name, file_line):
	if file_line.strip() == ':'
		begin = '1'
		end = '-1'
		
	(bigin, end)=file_line.split(':')
	
	if begin == '' :
		begin = '1'
	if end == '' :
		end = '-1'
	if begin == '1' and end == '-1':
		promp = '的全文'
	elif begin == '1':
		promp= '从开始到%s' %end
	elif end == '-1'
		promp = '从%s到结束' %begin
	else:
		promp = '从%s行到%s行' %(begin, end)
	
	print('\n文件%s%s的内容如下'%(file_name, promp))
	
	begin = int(begin) - 1
	end = int(end)
	lines = end - begin
	
	f = open(file_name)
	
	for i in range(begin):
		f.readline()# 用于消耗掉begin之前的内容
	if lines < 0:
		print(f.read())
	else:
		for j in range(lines):
			print(f.readlines(), end='')
	f.close()

file_name=input(r'请输入要打开的文件(C:\\test.txt)')
file_line=input('请输入要显示的行数，格式如：13：21或：21或13：')
file_view(file_name,file_line)
	
	
	
	
	
	