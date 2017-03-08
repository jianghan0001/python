def add(a,b):
	
	return a+b
def subtract(a,b):
	print("substracting %d-%d" %(a,b))
	return a-b
def mutiply(a,b):
	print("mutiply %d*%d" %(a,b))
	return a*b
def divide(a,b):
	print("dividing %d/%d" %(a,b))
	return a/ b
	
print ("Let's do some math with just functions!")

age=add(30,5)
height=subtract(89,4)
weight=mutiply(87,89)
iq=divide(999,33)
print ("------------second part")
print(age)
print ("------------third part")
print(height)
print ("------------forth part")
print(weight)
print ("------------fifth part")
print(iq)
print ("------------last part")
what=add(age,subtract(height,divide(weight,mutiply(age,2))))
print ("------------third part")
print("this is", what )
