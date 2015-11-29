def convert(arg):
	if(arg in "ABC"):
		return 2
	elif(arg == 'D' or arg == 'E' or arg == 'F'):
		return 3
	elif(arg == 'G' or arg == 'H' or arg == 'I'):
		return 4
	elif(arg == 'J' or arg == 'K' or arg == 'L'):
		return 5
	elif(arg == 'M' or arg == 'N' or arg == 'O'):
		return 6
	elif(arg == 'P' or arg == 'Q' or arg == 'R' or arg == 'S'):
		return 7
	elif(arg == 'T' or arg == 'U' or arg == 'V'):
		return 8
	elif(arg == 'W' or arg == 'X' or arg == 'Y' or arg == 'Z'):
		return 9
	else:
		return -1



user_input = input("Enter a letter: ").upper()
print(convert(user_input))
