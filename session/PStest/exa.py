num = 7
if num > 2:
    print(num)
    num -= 1
print(num)

x=5
y=0
z=x
while z!=0:
    y=y+x
    z=z-1
print(y)

a=int(input('please enter an integer.'))
b=0
while b**3 <a:
    b=b+1
if b**3 != a : #because of b**3<a so b**3=a will be wrong so only b**3 !=a will work here
    print('gundan')
else:
    print(b)


a=int(input('give me a number'))
b=0
while b**3<abs(a):
    b=b+1
if b**3 !=abs(a):
    print('gundan')
else:
    if a<0:
        b=-b
    print(b)

cube=2
for guess in range(cube+1):
    if guess**3 == cube:
        print(guess)

cube=27
for guess in range(abs(cube)+1):
    if guess**3 >=abs(cube):
        break
if guess ** 3 != abs(cube):
    print('gundan')
else:
    if cube<0:
        guess=-guess
    print(guess)









