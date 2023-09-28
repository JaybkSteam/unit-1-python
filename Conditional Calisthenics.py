#Exercise 1:
#Check if an integer is even and greater than 10.
#Return True if both conditions are met, False otherwise.

number1 = float(input('Enter number: '))
if number1 >= 10 :
  print(True)
elif number1 < 10:
  print (False)
else:
  print(False)
  #For this i  used a conditonal statement to check if th number the user put is greater then or less and 10
  # and depending on the numbe it would print out false or true


#Exercise 2:
#Determine the ticket price based on age and student status.
#Price is $10 if under 18 or a student, $20 otherwise.

Age = float(input('Enter number: '))

if Age <= 18:
  print('Your Ticekt cost 10$')
elif Age > 18:
  print ("Your ticket cost is 20$")
#for the i created a function called age and made the user input a number and then use a conditonal statement to check if 
#the number is greater than or less than 18







#Exercise 3:
#Prompt the user to enter a fruit name. Check if the fruit is in the list. 
#If it is, print "Yes, that fruit is in the list." 
#If it's not, print "No, that fruit is not in the list."

fruits = ['Melon', 'Apple', 'Orange', 'Banana', 'Strawberry',]

userfruit = (input('Enter your  Fruit:'))

if userfruit == fruits:
  print ('your fruit is the list')
else:
   print('Your fruit is not in the list')
#for this i just made a list called fruits it made it so that if the user input is equal to what the list fruits is then it 
#would print your fruit is in the list if not it would say its not in the list.


#Exercise 4:
#Check if a year is a century year and a leap year.
Year = int(input("Enter a year: "))
if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a leap year".format(Year))

elif (Year % 4 ==0) and (Year % 100 != 0):
    print("{0} is a leap year".format(Year))
    
    
elif (Year % 4 ==0) and (Year % 400 != 0):
    print("{0} is century year".format(Year))


else:
    print("{0} is not a leap year".format(Year))



#Exercise 5:
#Calculate the cost of shipping for an online order based on the order weight and destination zone. 
#The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
#If the order weight is less than 0 kg, return an error message.

wpk =  int(input(" what is the weight of package"))
area = input (f"what zone do you live in")
Zonea = 5
zoneb = 7 
print('zonea')
print('zoneb')

if area == Zonea:
    print ("your price is 5$ per kilogram")
elif area == zoneb:
    print(" your price is 7$ per kilogram")

#Exercise 6:
#Determine the type of a triangle based on side lengths.
#Equilateral, Isosceles, Scalene, or Not a triangle.#
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
