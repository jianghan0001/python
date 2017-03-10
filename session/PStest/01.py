print('think a number')
high=100
low=0
da=False
while True:
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
