from sys import argv

script, user_name= argv
prompt='>'

city=input("please enter your birth place"+prompt)
print ("Hi %s from %s. I'm the %s script." %(user_name, city,script))
print("I'd like to ask you some questions")
print ("Do you like me %s?"% user_name)

likes=input(prompt)

print ("What is the weather in %s"% city)

weather = input(prompt)

print("What kind of computer do you have?")
computer=input(prompt)
print('''
So you said %r about liking me.
the weather in your city is %s
But I can't fell it because I am a robot.
and you have a %r computer. Nice''' %(likes,weather,computer))