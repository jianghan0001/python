# replace a letter in a word
s= 'hello'
s= 'y'+s[1:]
#now s should be yello

s= 'abcdef'
s[::-1] #s should be fedcba  so here -1 means reverse
s[-1] #s should be fedcba
s[2:5] #def start at 0 end before 5(not include 5)

i=0
word=input('please give me a word')
for i in range(len(word)):
	print(word[i])
	i=i+1
	
i=0
word=input('please give me a word')
while i < len(word):
	print(word[i])
	i=i+1
	
#bisection method to find square root
x=25
high=x
low=0.0
ans=(high+low)/2.0
epsilon=0.01
while abs(ans**2-x)>epsilon:
	if ans**2 < x:
		low= ans
	else:
		high=ans
	ans=(low + high)/2.0
print(ans)


#guess a number by bisection
print('think a number')
high=100
low=0
da=False
while not da:
    ans=(high + low)//2
    jin=input('%d is c or h or l' %ans)
    if jin=='c':
        print('oh yeah!')
        da=True
    elif jin=='h':
        high= ans
    elif jin== 'l':
        low= ans
    else:
        print('gundan')
print('Your number is %d' %ans)
