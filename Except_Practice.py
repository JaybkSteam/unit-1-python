try:
 age = int(input('Enter your age: '))
 faveNum = int(input("What's your favorite number: "))
except:
 print("you did put in a number")
if age <= 21:
    print('you are now allowed inside, you are not old enough.')
else:
    print('You are able to enter ')

try:
   print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
   print('If zero as your favorite number just try again with a differnt one')