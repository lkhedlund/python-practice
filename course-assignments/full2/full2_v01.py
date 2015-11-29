# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Satisfaction calculator by Lars Hedlund.
Version: 0.0
Features: (1) Ask for input (2) Calculate grade point (3) calculate fun point
(4) Calculate satisfaction
Language: Python 3.3
"""
import random

# Starts by asking the user for time spent studying and having fun.
print ("Please input how much time you've spent studying and having fun.")
print ("Total hours should be equal to 20 hours.\n")

hours_spent = 0 # flag for while loop
while (hours_spent != 20):
    studying = int(input("How much time did you spend studying? "))
    fun = int(input("How much time did you spend having fun? "))
    hours_spent = studying + fun
    if (hours_spent != 20):
        print ("Hours were equal to %d. Please try again." % hours_spent)
    else:
        print("Thank you for your input.\n")

# this function takes a variable and returns the grade point.
# the grade point is based on a probability and the value of the variable.
def hours_studying(hours):
    prob = random.randint(1,100)
    if (hours == 0 and prob >= 51): # grade  for first group (0 hours)
        return 1
    elif (hours == 0 and prob <= 50):
        return 0
    elif ((1 <= hours <= 9) and prob >= 96): # second group (1-9 hours)
        return 4
    elif ((1 <= hours <= 9) and (91 <= prob <= 95)):
        return 3
    elif ((1 <= hours <= 9) and (66 <= prob <= 90)):
        return 2
    elif ((1 <= hours <= 9) and (41 <= prob <= 65)):
        return 1
    elif ((1 <= hours <= 9) and prob <= 40):
        return 0
    elif ((10 <= hours <= 17) and prob >= 81): # third group (10-17 hours)
        return 4
    elif ((10 <= hours <= 17) and (61 <= prob <= 80)):
        return 3
    elif ((10 <= hours <= 17) and (41 <= prob <= 60)):
        return 2
    elif ((10 <= hours <= 17) and (21 <= prob <= 40)):
        return 1
    elif ((10 <= hours <= 17) and prob <= 20):
        return 0
    elif ((18 <= hours <= 20) and prob >= 61): # last group (18-20 hours)
        return 4
    elif ((18 <= hours <= 20) and (36 <= prob <= 60)):
        return 3
    elif ((18 <= hours <= 20) and (11 <= prob <= 35)):
        return 2
    elif ((18 <= hours <= 20) and (6 <= prob <= 10)):
        return 1
    elif ((18 <= hours <= 20) and prob <= 5):
        return 0
    else:
        print ("Something went wrong. Please try again.")

# this function calculates the amount of fun
def fun_had(hours):
    return round(hours / 6)

# calculates satisfaction using both functions and the user's input
grade_point = hours_studying(studying)
fun_point = fun_had(fun)
satisfaction = grade_point + fun_point

# final output
print ("Let's take a look at how satisfied you are...")
print ("You studied for %d hours and received a grade of %d." % (studying, grade_point))
print ("You had fun for %d hours and received a fun score of %d.\n" % (fun, fun_point))
print ("All said and done, your satisfaction is %d." % satisfaction)
