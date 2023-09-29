#1. Simple Counter:
#Write a program that uses a while loop to print numbers from 1 to 10.
i = 1
while i < 11:
  print(i)
  if i == 11:
    break
  i += 1




#2. Countdown:
#Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
i=10
while(i>=1):
   print(i)
   i=i-1



#3. Factorial Calculation:
#Write a program that calculates the factorial of a given number using a while loop.
def factorial(n):
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1
    return f



#4. Password Guessing Game:
#Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.

psw = "Jaylin"
guess = ""
while guess != psw: 
   guess = input(" Put password:")
   if guess == psw:
      print("right password")
else:
   print("Wrong password")
#for this code a made a function called psw that would be the passwrd that im trying to guess and function called guess that would be 
#guess the user


#5. Sum of Digits:
#Write a program that calculates the sum of the digits of a given number using a while loop.
tot = 0
number = 1
while number > 0:
    number = int(input('Enter a number: '))
    if number > 0:
        tot = tot + number
print("The sum of the numbers is", tot)
# so for i created a functionl called tot that equal 0 that will stop the code from runing when u done and then i just used while and if 
#so the code can run properly and using operators so that the total + the numbers you put can be added together.
# for this code it will keep asking you to put in a number and to find out the total sum of all those number u just have to press 0/



#6. Fibonacci Series:
#Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.

def printFibonacciNumbers(n):
  
    fn1 = 0
    fn2 = 1
    if (n < 1):
        return
    print(fn1, end=" ")
    for x in range(1, n):
        print(fn2, end=" ")
        next = fn1 + fn2
        fn1 = fn2
        fn2 = next
  
  

printFibonacciNumbers(7)