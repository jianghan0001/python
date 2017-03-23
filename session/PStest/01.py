x=25
high=x
low=0
ans=(high+low)/2
epsilon=0.01
while (ans**2-x)>epsilon:
    if ans**2>x:
        ans=high
    else:
        ans=low
    ans
print(ans)
