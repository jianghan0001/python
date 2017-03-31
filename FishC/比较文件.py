#编写一个程序，比较用户输入的两个文件，如果不同，娴熟出所有不同处的行号和第一个不同字符的位置






def file_compare(file1, file2)
	f1 = open(file1)
	f2 = open(file2)
	deffer = []
	count = 0
	
	for line1 in f1:
		line2 = f2.readlines()
		count += 1
		if line1 != line2:
			differ.append(count)
	f1.close()
	f2.close()
	return differ
file1= input('please enter first file name!')
file2= input('please enter second file name!')
differ = file_compare(file1, file2)

if len(differ) == 0:
	print('They are same!')
else:
	print('There are total %d differents', %len(differ))
	for each in differ:
		print ('Locate at %d line' %each)