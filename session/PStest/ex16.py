from sys import argv
from os.path import exists
#os.path检查文件是否存在
script, from_file,to_file=argv
#定义2个变量 from_file and to_file
print ("Copying from {0} to {1}".format(from_file,to_file))

in_file=open(from_file)
indata=in_file.read()
#in_file只存了一个磁盘的地址
#indate是正八经的内容
print ("The input file is %d bytes long" %len(indata))
print ("Does the output file exists? %r" %exists(to_file))

print("Ready, hit return to continue, CTRL-C to abort.")
input()
#out_file=open(to_file,'w')
#out_file.write(indata)
#if we can append
out_file=open(to_file,'a')
out_file.write(indata)
print ("Alright all done.")

out_file.close()
in_file.close()