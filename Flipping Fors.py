#Exercise 1:
#Write a program to print each character of a given string using a for loop.

Cars = ["Ferrari","Lamborghini"," Nissan GT-R"]

for x in Cars:
    print(x)




#Exercise 2:
#Write a program to calculate the sum of elements in a list using a for loop.
total = 0
 
# creating a list
list = [16, 5, 17, 10, 3]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list)):
    total = total + list[ele]
 
# printing total value of all the numbers in the list
print("The sum of all the elements in the list is: ", total)
#Exercise 3:
#Write a program to print the length of each word in a sentence using a for loop and a list.

q="It's october It's spooky month"
#splitting the words in a  string
b=q.split(" ") 
for i in b: 
  #checking the length of words
  if len(i)%2==0: 
    print(i)
#Excercise 4:
#Write a program that creates a dictionary (atleast 4 key:value pairs) and then
#iterates through a dictionary and prints the result
dictionary = {'a': 'Ferrari', 'b': 'Lamborghini', 'c': 'Nissan GT-R'}

for key in dictionary:
    print(key, dictionary[key])

#In a comment, answer the following, what do you notice about the output of your code?
#Is it what you expected?
#The oppot of my code is what i expected because i expected it to be just like the first task just with 1 exta step
#so i did not find it confusing
