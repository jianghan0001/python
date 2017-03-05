x="There are {} types of people.".format(10)
binary="binary"
do_not="don't"
y="Those who know {0} and those who {1}.".format(binary,do_not)
z="Those who know {1} and those who {0}.".format(binary,do_not)
print (x)
print (y)
print (z)
print ("I said {0}.".format(x))
print ("I also said: '%s'." % y)

halarious=False
joke_evaluation='Is the joke so funny?{}'
print (joke_evaluation.format(halarious))

print(x+y)

#不同类型的变量相加是不被允许的 例如 string+10 not work
#string + '10' work