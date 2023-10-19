#Task 1: People Class
#Define a class called Person with attributes name and age.
#Then, write a method within the class to introduce the person with their name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # create display method fro Person class
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
        
P = Person("Jaylin Edouard", 16)
P.display()

#Create a new object using this new class, and call the method you created.

#Task 2: Animals Speak
#Create a base class Animal with a empty method called speak. 
class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place

    def speak(self, adverb):
        print("%s just did a %s %s" % (self.name, adverb, self.speechtype))

    #getallinfo method, get's all the parametrs of both classes.
    def getallinfo(self):
        print("%s is a %s %s %s, sitting on the %s" % (self.name, self.gender, self.breed, self.kind, self.place))

#This class inherits kind and place arguments from Animal class (which can work for any animal)
#Initiates a Dog object with name, gender and breed parameters.

class Dog(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.speechtype = "woof";
        Animal.__init__(self, 'Dog', 'Ground')


#Cat class inherits the paramets of use for a Cat (similar things) like name, gender and breed, which they both share, also the getallinfo method and initiate them. 
class Cat(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.speechtype = "meow";
        Animal.__init__(self, 'Cat', 'Ground')


#Here I create 3 objects, 2 dogs and 1 cat with selected arguments.
#And check for some methods on the objects.
cortez = Dog('Cortez', 'Male', 'Yorkshire Terrier')
Piglet = Dog('Piglet','Female','chihuahua')
Pepper = Cat('pepper','Female','Persian')
Pepper.getallinfo()
Pepper.speak('soft')
Piglet.getallinfo()
cortez.speak('loud')

#Then create two subclasses, Dog and Cat, each with their own speak method. 

#Create objects using these subclasses and call the speak method.

#Task 3: Banking
#Create a class BankAccount with attributes balance and owner. 

#Include methods for depositing and withdrawing money, which should modify the balance attribute.

#Test these methods with instances of the classlass Bank_Account:
class Bank_Account:
    def __init__(self):
        self.balance=0
        print(" HTM Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()