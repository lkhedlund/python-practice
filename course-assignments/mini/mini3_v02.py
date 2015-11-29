def user_phone():
	while True:
		user_input = raw_input("Please enter your phone number: ")
		for i in user_input:
			if str(i[0]) == "0":
				return False
			else:
				print "Done"
user_phone()
