#模块是可用代码段的打包，是一个包含所有已定义的函数和变量的.py文件
import random
secret = random.randint(1,10)
OS 模块--operation system 不care是啥系统
import OS
os.getcwd()#返回当前工作目录
os.chdir(path 'E:\\')#改变工作目录
os.listdir(path 'E:\\')#显示目录下文件
os.mkdir(path 'E:\\A' )#创建单层目录
os.makedirs(path'E:\\C\\B\\A')#创建多层目录.
os.remove(path)#删单独文件
os.rmdir(path 'E:\\C\\B\\test.txt')#要目录为空才能删除目录
os.rename(old, new)
os.system(command)#运行系统shell命令 os.system('cmd') 打开dos
os.listdir('.')#当前目录文件夹
os.listdir('..')#上一级目录的文件夹

os.path模块
basename(path) #去掉路径返回文件名
dirname(path) #去掉文件名 返回路径 配合listdir用
join(path1, path2)
split()#分割文件名和路径
splitext(path)#分离文件名和拓展名
getsize(file)#字节
getatime()#最近访问时间 
getctime()#创建时间
getmtime()#修改时间
import time的time.gmtime(os.path.getatime(file))才能正确显示可读时间
time.localtime()
#判断
exist(path)
isabs()