#Exercise 1:
#Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
#just used for and range and then print to print out number 1 throught 10
#Exercise 2:
#Write a program to count by 10s from 900 to 1000
def number10to1000(input_number):
    result = [0]
    i = 1
    while (I := i*10) <= input_number:
        result += range(i, I, i)
        i = I
    result += range(i, input_number+i, i)
    return result
print(number10to1000(1000))

# created a variable called number10t0100 so that it can print out the code
# used conditoanl and range so that the program can caulacte by 10 when it reached the number 10
#  and keep adding by 10 untill it reaches the final the number its allowed to

#Exercise 3:
#Write a program that counts form 1-100 by 9
def number1to100(input_number):
    result = [0]
    i = 1
    while (I := i*9) <= input_number:
        result += range(i, I, i)
        i = I
    result += range(i, input_number+i, i)
    return result
print(number1to100(1000))
#just copuied the code from exercise 2 and changed the 10 in the while part of the code to a 9 so that
#it can count from 9 instead of 10


#Exercise 4:
#Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
sum = 0 
for i in range(1, 11): 
  sum += i 
print(sum) 
# created a function called sum and then had the sum be calucated to all the number that are in the range of 1 to 10.

#Excercise 5:
#Uncomment the following code and run it. Then answer the following:
# What is the ouput of the code?

# Explain the iterative process that this code executes to get that output

rows = 5
 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
     #The out of this code is that it post it post 5 lines of code that each have a differnt number of 
     # * that start from 1 on line 1 to 5 on line 5.