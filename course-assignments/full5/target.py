# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Target Module
AUTHOR: Lars Hedlund

MAIN FEATURES:
(1) Tally X (2) Tally Y (3) Probabilty of X (4) Probability of Y
Methods:
(1) init (2) create interaction (3) return end report

BUGS: None known
VERSION: 0.4

ABOUT:
This module contains the Target Class.
"""
# Import DEBUG if present
try:
    import DEBUG
except ImportError:
    pass
# Python Libraries
import sys
import random

class Target:

    def __init__(self, x, y):
        self.tallyX = 0
        self.tallyY = 0
        self.probX = x
        self.probY = y

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

    def reportEnd(self):
        # FUNCTION: Data for reportEnd in PURSUER
        # INPUT: none
        # RETURN: integer
        return self.tallyX, self.tallyY
