print("Welcome to your todo list!\n")
tasks = []
# creating a function called tasks so i can put
while True:
  putask = input("Pick a option  \n 1. Add a task \n 2. delete a task \n 3. Exit code \n   Put number: ")
  #created another function called putask and made the function have 3 outputs that would let the user 
  #pick a option and each option would do something else later in the code.

  print("")
  if putask == "1":
    task = input("Please type in the task you'd like to add: ")
    tasks.append(task)
  elif putask == "2":
    deletetask = input("Please type in the number of the task you'd like to remove: ")
    tasks.remove(tasks[int(deletetask)-1])
  elif putask == "3":
    break
  # here i used conditonal statements so  that i can add,delete and select certain tasks. and after the conditonal statment code 
  # is finished i used the break command to stop the code from runing again.
  # print todo list
  print("")
  print("Here's your updated list: ")
  for i in range(0,len(tasks)):
    print(str(i+1) + ". " + tasks[i])
  print("") 

  # this code just prints your current list of all your tasks  
  # and prints when you update your list my adding or removing one of your tasks.