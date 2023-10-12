#Exercise 1:
#Write a Python program that prints the current date and time using the datetime module.
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
#just used the datetime module command to print that you can find on w3resources and weschools


#Exercise 2:
#Write a Python program that prints the current date and time using the datetime module.
#Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))



#Exercise 3:
#Using the strptime function, convert two strings into dates.
#Then find the difference in days between the two.
import datetime 

d1_str = "oct 11 2023"
d2_str = "dec 12 2023"

fmt = "%b %d %Y"

d1 = datetime.datetime.strptime(d1_str, fmt).date()
d2 = datetime.datetime.strptime(d2_str, fmt).date()

delta = d2 - d1
print(delta)
print(delta.days)

#Excercise 4:
#Write a program that asks the user for their birthdate and calculates their current 
#age using the datetime module.
from datetime import datetime, timedelta

# Get the current date
now = datetime.now()

# Ask the user for their date of birth
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()

# puts the user input into a datetime module
birthday = datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate the difference between the current date and the birthday
difference = now - birthday

# Calculate the user age in years
age_in_years = difference.days // 365

print(f"You are {age_in_years} years old.")