x='There are {} types of people.' .format(10)
binary='binary'
do_not='do not'
y='those who know {0} and those who {1}.' .format (binary,do_not)
print (x)
print (y)
print (x+' '+ y)
print (x+'10')

print ("I said {0}." .format(x))
print ("I also said '%s'." %y) #'' 是扯淡的 会显示出来
halarious= False
joke_evaluation="Is the joke so funny? {}"#括号表示放了个占位符 可以以后放变量
print (joke_evaluation.format(halarious))
print (x+y)#字符串拼接