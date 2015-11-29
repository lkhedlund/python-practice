# Testing classes for the first time!

class Animal:
    name = str()
    age = int()

    def __init__(self):
        self.name = "no name"
        self.age = -1

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, new_name):
        self.name = new_name
        return self.name

    def setAge(self, new_age):
        self.age = new_age
        return self.age

    def makeSound(self):
        print("meow")

cat = Animal()
name = cat.getName()
age = cat.getAge()

print(name, age)

name = cat.setName("Meowzers")
age = cat.setAge("99")

print(name, age)

cat.makeSound()
