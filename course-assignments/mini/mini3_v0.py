# 

"""
HEADER: Asks the user for a valid phone number. 
"""

def phone_number():
	user_input = int(raw_input("Please enter your phone number "))
	while (user_input > 7) or (user_input < 0):
		for i in user_input:
			if i[0] == 0:
				user_input
			else:
				print "Thank you! Valid phone number entered: %d" % user_input
			
phone_number()