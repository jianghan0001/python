from sys import argv

script, filename=argv

txt=open(filename)
#txt（指针）是文件内容所在的file的地址 open 打开一个文件 只打开 没读
# python 在跟系统打交道
print ("Here's you file {}.".format(filename))
print (txt.read())

txt.close()
#运行script的东西时要给个值 在edit里面
print ("Type the filename again:")
file_again=input('> ')
txt_again=open(file_again)

print (txt_again.read())

txt_again.close()