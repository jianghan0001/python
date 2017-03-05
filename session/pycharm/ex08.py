formatter='%r %r %r %r'
# r%表示rows 原始数据 给啥出啥，你加工
print(formatter %(1,2,3,4))
print('%s %s %s %s' %('one','two','three','four'))
print(formatter %('one','two','three','four'))
print(formatter %(True,False,False,True))
print(formatter %(formatter,formatter,formatter,formatter))
#因为有‘%’所以第一个formatter取代第一个%r