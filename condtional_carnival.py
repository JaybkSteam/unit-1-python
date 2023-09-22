#TASK 1 Even or Odd
#Determine if a number is even or odd.
num = int(input("Enter a number to see whether or not if it is even or odd : "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    # i used if else statment to help check if number is  even or odd 
	

#TASK 2 Positive, Negative, or Zero:
#Determine if a number is positive, negative, or zero.
#EXTRA CREDIT: Tell the user if they did not enter a valid number
num = float(input("Enter a number: "))
if num > 0:
   print("This is a Positive number")
elif num == 0:
   print("Zero")
else:
   print("This is a Negative number")
# for this i decide to use if else statement to help with decdending if the number is postive or negative or just a zero.


#TASK 3: Largest of Three
#Find and print the largest of three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)




#TASK 4: Leap Year
#Determine if a year is a leap year or not.

Year = int(input("Enter a year: "))
if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a leap year".format(Year))

elif (Year % 4 ==0) and (Year % 100 != 0):
    print("{0} is a leap year".format(Year))

else:
    print("{0} is not a leap year".format(Year))



#TASK 5: Vowel or Consonant:
#Identify if a character is a vowel or consonant.
def vowelOrConsonant(x):
  
    if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")
  

vowelOrConsonant('c')
vowelOrConsonant('e')
    
