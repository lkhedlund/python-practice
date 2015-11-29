# class Parent is-a object
class Parent(object):
    # Parents has-a function, override, which takes the parameter self
    def override(self):
        # function override() prints phrase
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

# class Child is-a Parent        
class Child(Parent):
