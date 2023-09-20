#task 1: Create a float variable, and then convert it to an integer
#Print both the original variable and the converted integer.

num = 1.6 
print('type:',
      type(num).__name__) 
num = int(num)  
print('converted value:', num,
      ', type:', type(num).__name__) 

print (num)


#task 2: Write code that takes a number as input and prints whether 
#it's positive, negative, or zero using if-elif-else statements.

num = float(input("enter number"))
if num > 0:
   print("positive number")
elif num == 0:
   print("Zero")
else:
   print("negative number")

   #task 3: Write code that takes two numbers as input (an integer and a float), 
#performs addition, subtraction, multiplication, and division, and prints the results.
num1 = 8.0
num2 = 4.2
print (num1 * num2 )
print (num1 - num2)
print (num1 + num2)
print (num1 / num2)



#Task 4: Create a dictionary with keys as fruit names and values as their respective quantities. 
#Then print out the quantity of one of the fruits.

Dict = {1: 'Peach', 2: 'Mango', 3: 'Strawberry'}
print(Dict)



#Task 5:Create a string variable with that is a list of numbers and convert that string into a tuple.
#Then print out the both the original string and tuple.




numlist = "17, -23, 0, 10, 6, 16, 12,"

print ("The string is : " )
print(numlist)

my_result = tuple(map(int, numlist.split(', ')))

print("The tuple after converting from a string is - ")
print(my_result) 
print (numlist)
