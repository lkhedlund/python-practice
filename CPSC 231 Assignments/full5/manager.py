# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Main Program (Pursuer/Target Simulation)
AUTHOR: Lars Hedlund

MAIN FEATURES:
(1) prompt for interactions (2) prompt for x-type probability
(3) instatiate pursuer and target (4) Adapt behaviour after two
turns

BUGS: None known
VERSION: 0.4

ABOUT:
From assignment overview: "A dating simulator
for fictional life forms called the "Tims" (Tam's simulated life
forms) 1. There are two types of Tims in this simulation: a
'pursuer' and a 'target'. The target is the object of the pursuer's
desire. In the full version of the program, the goal of the pursuer
is to have a successful date with the target. The target's behavior
is purely random. The date consists of a number of social interactions.
If by the end of the date the proportion of successful interactions
is 50 percent or greater then the date is considered successful otherwise
it's deemed a failure. Two types of reports will show statistics
on various aspects of the date."

LIMITATIONS:
If I was to design this assignment I would remove a lot of the
redundant code. Target and Pursuer both 'act the same', so a Class
they can both use to pull attributes and methods from would be far
more efficient. I would choose this approach for the assignment if
the guidelines didn't require me to follow the strict rules of
each having their own attributes and methods. I would also add
create a checkInput function for the user input, which I originally
created but removed because of the "manager cannot contain more
than two functions" requirement. 
"""
# Imports
from pursuer import Pursuer
from target import Target
import random
# Import DEBUG if present
try:
    import DEBUG
except ImportError:
    pass

def main():
    # total number of interactions between 1 and infinity
    validInter = False # flag for a valid user input
    while validInter == False:
        try:
            totalInter = int(input("Enter total number of interactions (greater than or equal to 1): "))
        except ValueError:
            print("Do not enter non-numeric values.")
        else:
            if (totalInter >= 1):
                validInter = True
            else:
                validInteractions = False
                print("Input is out of range.")
    # Set the target's probability of X or Y
    validProb = False # flag for a valid user input
    while validProb == False:
        try:
            probX = int(input("Probability of X-type Interactions for the target (1-100): "))
        except ValueError:
            print("Do not enter non-numeric values.")
        else:
            if (1 <= probX <= 100):
                validProb = True
            else:
                validProb = False
                print("Input is out of range.")
    probY = 100 - probX # probabilty of Y interactions
    #DEBUG
    DEBUG.dprint("total # interactions: %r" % totalInter)
    DEBUG.dprint("probability of X: %r" % probX)
    # Pursuer class takes the two probabilities
    aPursuer = Pursuer(totalInter)
    aTarget = Target(probX, probY)
    # Main Loop
    i = 0 # flag
    while i < totalInter:
        # create an interaction for the pursuer and the target
        interP = aPursuer.createInteraction()
        interT = aTarget.createInteraction()
        # DEBUG
        DEBUG.dprint("aPursuer Interaction: %r" % interP)
        DEBUG.dprint("aTarget Interaction: %r" % interT)
        DEBUG.dprint("i: %r" % i)
        # record and display the result
        result = aPursuer.reportInteraction(interP, interT)
        print(result)
        i += 1 # update flag
        if i >= 2:
            aPursuer.adaptBehaviour(interP, interT)
    targetX, targetY = aTarget.reportEnd()
    aPursuer.reportEnd(targetX, targetY)

main()
