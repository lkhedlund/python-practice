# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Pursuer Module
AUTHOR: Lars Hedlund

MAIN FEATURES:
Attributes:
(1) Tally X (2) Tally Y (3) Probabilty of X (4) Probability of Y
(5) Tally Successfull Interactions (6) Accept total number of
interactions
Methods:
(1) init (2) create interaction (3) report each interaction
(4) create 'end-of-sim' report (5) adapt behaviour

LIMITATIONS:
(1) Behaviour adaptation is best at 500+ samples. While it still
matches behaviour at less than 100, it isn't perfect.

BUGS: None known
VERSION: 0.4

ABOUT:
This module contains the Pursuer Class.
"""
# Import DEBUG
try:
    import DEBUG
except ImportError:
    pass
# Python Libraries
import random

class Pursuer:

    def __init__(self, totalInter):
        self.tallyX = 0 # number of X interactions
        self.tallyY = 0 # number of Y interactions
        self.probX = 50
        self.probY = 50
        self.success = 0
        self.total = totalInter # total number of interactions

    def createInteraction(self):
        # FUNCTION: Creates an interaction based on the probabilty of X
        # and y from the MANAGER file.
        # INPUT: none
        # RETURN: string

        # Add a number of Xs or Ys based on the probability set in MANAGER
        choices = ["X"] * self.probX + ["Y"] * self.probY
        # Pull either X or Y from the list
        interaction = random.choice(choices)
        # Tally choices
        if interaction == 'X':
            self.tallyX += 1
        else:
            self.tallyY += 1
        # DEBUG
        DEBUG.dprint(interaction)
        DEBUG.dprint("tallyX: %r, tallyY: %r" % (self.tallyX, self.tallyY))
        # returns
        return interaction

    def reportInteraction(self, interP, interT):
        # FUNCTION: Reports the interaction that took place
        # INPUT: string, string >> takes the returned interaction
        # parameters from aPursuer and aTarget createInteraction()
        # RETURN: string

        # Number of successful matches
        if (interP == interT):
            match = "Matched Behaviour"
            self.success += 1
        else:
            match = "Mismatched Behaviour"
        result = "Target behavior: %s\tPursuer behavior: %s\t%s" % (interP, interT, match)
        return result # NB: may want to return match later, for behaviour module

    def reportEnd(self, targetX, targetY):
        # FUNCTION: Reports the final interactions that took place
        # INPUT: integer, integer
        # RETURN: none
        DEBUG.dprint("success: %r\ttotal: %r" %(self.success, self.total))
        proportion = (self.success / self.total) * 100
        DEBUG.dprint("proportion: %r" % proportion)
        print("ANALYSIS OF ALL INTERACTIONS:")
        print("Target: No. of Xs = %i\tNo. of Ys = %i" %(targetX, targetY))
        print("Pursuer: No. of Xs = %i\tNo. of Ys = %i" %(self.tallyX, self.tallyY))
        print("Number of successful matches: %i" % self.success)
        print("Proportion of successful matches: %0.1f" % proportion)
        if proportion >= 50:
            print("You were successful! Congratulations!")
        else:
            print("You were not successful...Better luck next time.")

    def adaptBehaviour(self, interT, interP):
        # FUNCTION: Adapts the behaviour of the pursuer to the target
        # INPUT: Interaction for TARGET and PURSUER
        # RETURN: none

        # If the target exhibits 'matching' qualities, it increases
        # probability of that outcome and reduces the probability of
        # the opposite outcome
        if (interP == "X") and (interT == "X") and (self.probX < 100):
            self.probX += 1
            self.probY -= 1
        elif (interP == "Y") and (interT == "Y") and (self.probY < 100):
            self.probY += 1
            self.probX -= 1
        else:
            pass
        DEBUG.dprint("InterP: %r, InterT: %r, probX: %r, probY: %r" %(interP, interT, self.probX, self.probY))
