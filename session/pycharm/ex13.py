from sys import argv #想象成从外面import一个东西进来 参数的一个数列 一个包
script, first, second, third=argv
#argv-argument variaty n-pack  in powelshell input value no comma needed 赋值从第二个开始
print("The script is called: ",script)
print("Your first variable is: ",first)
print("Your second variable is: ",second)
print("Your third variable is: ",third)

#argv 一个包 import 把里面写的东西拿进来
#第二句 有等号就是赋值 赋值只能往变量上赋值 左侧变量右侧值
#argv argument array   npack右侧是个数列 左侧从右侧拿值 按照顺序拿
#运行时直接在后面给参数到first second third 相当于往argv放3个值 数量要一致 不需要逗号 script可以忽略