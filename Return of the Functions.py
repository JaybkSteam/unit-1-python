#Task 1: Calculate the Square of a Number
#Write a function that takes an integer as an argument and returns its square.
def square(n):
  return n**2

number = int(input('Please enter a number: '))
number2 = square(number)
print(number2)
assert square

#Task 2: Calculate the Area of a Rectangle:
#Write a function that takes the length and width of a rectangle and returns its area.
def area_of_Rectangle(length, width):
    return length * width
length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the area of a Rectangle
area = area_of_Rectangle(length, width)

print("The Area of a Rectangle using", length, "and", width, " = ", area)
x = 8
y = 7
def area_of_Rectangle(x, y):
   return x + y
assert area_of_Rectangle(x, y) == 15

#Task 3: Convert Temperature from Celsius to Fahrenheit:
#Write a function that takes a temperature in Celsius and returns 
#The equivalent temperature in Fahrenheit using the correct formula

celsius_temp = 45
fahrenheit_temp = (celsius_temp*9/5)+32
print("The Fahrenheit equivalent of 45 celsius = ", fahrenheit_temp)






#Task 4: Calculate the Average of Numbers:
#Write a function that takes a list of numbers 
#and returns the average (mean) of those numbers.
from statistics import mean

num_list = [30, 55, 3, 10, 2]

average = mean(num_list)

print("Average: ", round(average,3))