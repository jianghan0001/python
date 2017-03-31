import os

all_file= os.listdir(os.getcwd())
type_dic={}

for each_file in all_file:
	if os.path.isdir(each_file):
		type_dic.setdefault('folder'，0)
		type_dic['folder'] += 1 
	else:
		ext = os.path.splitext(each_file)[1]
		type_dic.setdefault(ext, 0)
		type_dic[ext] += 1
for each_type in type_dic.keys():
	print('该文件夹下共有类型为【%s】的文件%d个'%(eachtype, type_dic[each_file]))