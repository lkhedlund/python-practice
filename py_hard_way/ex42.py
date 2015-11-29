## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Emplyee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet that is-a satan
mary.pet = satan

## Frank is-a employee that has-a name and 120,000
frank = Employee("Frank", 120000)

## Frank has-a pet that is-a satan
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a instance of Salmon
crouse = Salmon()

## harry is-a instance of Halibut
harry = Halibut()
