import os

all_file= os.listdir('.')
file_dic = {}

for each_file in all_file:
	if os.path.isfile(each_file):
	
		file_dic[each_file]= os.path.getsize(each_file)
		
		
for each in file_dic
	print('文件%s的大小是%dbytes'%(each[0],each[1]))