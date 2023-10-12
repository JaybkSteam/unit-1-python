# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def hello_function(name):
    print("Hello " + name)
hello_function("Jaylin")
# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(numbers):
    sum_numbers(1,2)
    print()


# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
def factorial(n): 
    nnn=1
    while n>1:
        nnn=nnn*n
        print(nnn)
        n-=1


# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even_number(n):
   return True if n % 2 == 0 else False
while True:
   number = int(input("Enter a number: "))
   if number == 0:
       break
   else:
       if is_even_number(number):
           print("Even")
       else:
           print("Odd")
        

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
def calculate_area(length,width):
    n=length * width  # mutiplies the numbers
    print(n)
    calculate_area(22,16)