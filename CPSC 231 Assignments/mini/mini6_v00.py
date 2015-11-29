# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial: 02

"""
TITLE: Animal Classes
AUTHOR: Lars Hedlund
FEATURES: Two animal classes with the same features
VERSION: 0.0
BUGS: None
"""

class Cat:

    def __init__(self):
        self.__name = "no name"
        self.__age = -1

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, new_name):
        self.__name = new_name

    def setAge(self, new_age):
        self.__age = new_age

    def makeSound(self):
        print("meow")

class Dog:

    def __init__(self):
        self.__name = "no name"
        self.__age = -1

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, new_name):
        self.__name = new_name

    def setAge(self, new_age):
        self.__age = new_age

    def makeSound(self):
        print("bark")

class Driver:

    def __init__(self):
        # instances of Cat and Dog
        aCat = Cat()
        aDog = Dog()
        # print name and age of Cat and Dog
        print("Dog\nName: %s\nAge: %i\n" % (aDog.getName(), aDog.getAge()))
        print("Cat\nName: %s\nAge: %i\n" % (aCat.getName(), aCat.getAge()))
        # Set Cat name and age
        aCat.setName("Tigger")
        aCat.setAge(7)
        # Print new cat name and age
        print("Cat\nName: %s\nAge: %i" % (aCat.getName(), aCat.getAge()))

Driver()
