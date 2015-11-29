# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Satisfaction calculator by Lars Hedlund.
Version: 0.2 (Cleaned up the if,elif,else statements)
Features: (1) Ask for input (2) Calculate grade point (3) calculate fun point
(4) Calculate satisfaction
Language: Python 3.3
"""
import random

def hours_studying(hours):
    """ Takes a variable and returns the grade point. The grade point is based on
    a probability and the value of the variable. """
    prob = random.randint(1,100)
    if hours >= 18: # Grade for 18-20 hours
        if prob >= 61:
            return 4
        elif prob >= 36:
            return 3
        elif prob >= 11:
            return 2
        elif prob >= 6:
            return 1
        elif prob >= 0:
            return 0
        else:
            print("Unexpected grade return. Please try again.")
    elif hours >= 10: # Grade for 10-17 hours
        if prob >= 81:
            return 4
        elif prob >= 61:
            return 3
        elif prob >= 41:
            return 2
        elif prob >= 21:
            return 1
        elif prob >= 0:
            return 0
        else:
            print("Unexpected grade return. Please try again.")
    elif hours >= 1: # Grade for 1-9 hours
        if prob >= 96:
            return 4
        elif prob >= 91:
            return 3
        elif prob >= 66:
            return 2
        elif prob >= 41:
            return 1
        elif prob >= 0:
            return 0
        else:
            print("Unexpected grade return. Please try again.")
    elif hours == 0: # Grade for 0 hours
        if prob >= 51:
            return 1
        elif prob >= 0:
            return 0
        else:
            print("Unexpected grade return. Please try again.")
    else:
        print("Unexpected error with hours provided. Please try again.")

def fun_had(hours):
    """ Calculate the amount of fun """
    return round(hours / 6)

def main():
    """
    The start of the program. First, ask the user for input.
    """
    print ("Please input how much time you've spent studying and having fun.")
    print ("Total hours should be equal to 20 hours.\n")
    hours_spent = 0 # flag for while loop
    while (hours_spent != 20):
        studying = int(input("How much time did you spend studying? "))
        fun = int(input("How much time did you spend having fun? "))
        hours_spent = studying + fun
        if (hours_spent != 20):
            print ("Hours were equal to %d, not 20. Please try again." % hours_spent)
        else:
            print("Thank you for your input.\n")
    # calculates satisfaction using the calculator functions and the user's input
    grade_point = hours_studying(studying)
    fun_point = fun_had(fun)
    satisfaction = grade_point + fun_point
    # final output
    print ("Let's take a look at how satisfied you are...")
    print ("You studied for %d hours and received a grade of %d out of 4." % (studying, grade_point))
    print ("You had fun for %d hours and received a fun score of %d out of 3.\n" % (fun, fun_point))
    print ("All said and done, your satisfaction is %d out of 5." % satisfaction)

main()
