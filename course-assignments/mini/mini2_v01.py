# HEADER: Dice to grade roller by Lars Hedlund
# Version: 0.0
# Features: (1) Roll Dice (2) Return letter grade
# Language: Python 3.3

# Import random from python library.
import random

# Function asks user to continue before providing an integer between 1-6. Integer returns
# a corresponding letter grade. 
def dice_roll():
	input ("Press any key to roll the dice ")
	roll = random.randint(1,6)
	grade_print = ("Your letter grade is...")
	if roll < 1:
		print ("Error: The roll was less than 1. Please try again.")
	elif roll > 6:
		print ("Error: The roll was greater than 6. Please try again.")
	elif roll == 1:
		print (grade_print)
		print ("W")
	elif roll == 2:
		print (grade_print)
		print ("F")
	elif roll == 3:
		print (grade_print)
		print ("D")
	elif roll == 4:
		print (grade_print)
		print ("C")
	elif roll == 5:
		print (grade_print)
		print ("B")
	elif roll == 6:
		print (grade_print)
		print ("A")
	else:
		print ("Something went wrong! Please try again.")

# Calls function
dice_roll()

