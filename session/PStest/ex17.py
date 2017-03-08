#method def开启一个function的body 要有名字，参数 用冒号开启 tab表示归属 
#function 
#规范 用tab表示归属上述function *args可以给任何多 里面能不能塔克是另一回事
# function后面别忘了“：”
def print_two(*args):#冒号 冒号 tab表示下面的语句归属于上面的
	arg1,arg2=args
#arg1 and arg2 are unpack 赋值
	print ("arg1: %r, arg2: %r"% (arg1,arg2))
	
def print_two_again(arg1,arg2):
	print ("arg1: %r, arg2: %r"% (arg1,arg2))

def print_one(arg1):
	print ("arg1: %r" %arg1)

def cheese_and_crackers(cheese_count, crackers):
	print ("You have %d cheeses!" %cheese_count)
	print ("you have %d crackers!" %crackers)
cheese_and_crackers (10, 20)
cheese_and_crackers (10+20, 20+40)

amount_of_cheese=100
amount_of_cracker=150

cheese_and_crackers(amount_of_cheese,amount_of_cracker)
def print_none():
	print ("got nothing")
print_two("Ted","Bear")
print_two_again("Teddy","Bear")
print_one ("Only one")
Print_none()