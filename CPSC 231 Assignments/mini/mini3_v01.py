# 

"""
HEADER: Asks the user for a valid phone number. 
"""
def phone_number():
	user_input = raw_input("Please enter your phone number ")
	while True:
		for i in user_input:
			if i[0] == 0:
				print "Invalid. Please try again."
			elif user_input > 7
		else:
			print "Thank you! Valid phone number entered: %s" % user_input
