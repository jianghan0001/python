#EX5
#数字是不可以作为变量名开头的
#camelCase 第二个单词首字母大写 驼峰
#PascalCase 所有单词首字母大写
#myName
#MyName

name='Sam'
age=30
height=180
weight=180
eyeColor='black'
teeth='White'
hairColor='Black'
# %s表示一个变量，%name表示代入的变量值 s-string f-float %5.3f表式总长度5 小数点后面3 d-int r-rowdata 
#顺序对应 注意没逗号
print ('let\'s talk about %s' %name)
print ('let\'s talk about {0}' .format(name))
print ('let\'s talk about', name)

print ('He is %d inches tall.' %height)
print ('He is {0} inches tall.' .format(height))
print ('He is %d pounds heavy.' %weight)
print ('He is {0} pounds heavy.' .format(weight))
print ('He gets %s eyes and %s hair.' %(eyeColor,hairColor))
print ('He gets {0} eyes and {1} hair.' .format(eyeColor, hairColor))
  