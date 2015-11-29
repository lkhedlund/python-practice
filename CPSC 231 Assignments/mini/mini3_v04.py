#Name: Lars Hedlund
#ID Number: 00308102
#Tutorial number: 02

"""
HEADER: Phone number validity checker by Lars Hedlund.
Version: 0.4
Features: (1) Ask user for input (2) Prompt for input again if invalid
Language: Python 3.3
"""

# Sets the flag for the while loop.
user_input = "invalid"

# The 'while loop' checks for a valid integer within a set range. 
# The range ensures that the first number entered will not be zero. 
print ("Please enter your seven digit phone number, without spaces or dashes, below:")
while user_input == "invalid":
	phone_number = int(input("> "))
	if phone_number < 1000000 or phone_number > 9999999:
		print ("Invalid input. Please try again.")
	else:
		print ("Thank you! The number you entered was valid: %d" % phone_number)
		user_input = "valid"
	
