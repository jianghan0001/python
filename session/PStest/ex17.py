#method def开启一个function的body 要有名字，参数 用冒号开启 tab表示归属 
#function 
#规范 用tab表示归属上述function *args可以给任何多 里面能不能塔克是另一回事
# function后面别忘了“：”
def print_two(*args):
	arg1,arg2=args
#arg1 and arg2 are n-pack 赋值
	print ("arg1: %r, arg2: %r"% (arg1,arg2))
	
def print_two_again(arg1.arg2):
	print ("arg1: %r, arg2: %r"% (arg1,arg2))

def print_one(arg1):
	print ("arg1: %r" %arg1)

def print_none():
	print ("got nothing")

print_two("Ted","Bear")
print_two_again("Teddy","Bear")
print_one ("Only one")
Print_none()


def cheese_and _crackers(cheese_count,crackers)
	print("You have %d cheeses!"% cheese_count)