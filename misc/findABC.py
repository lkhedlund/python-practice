def findABC(input_string):
	ABC_true = ""
	if len(input_string) < 2:
		return False
	else:
		for i in range(len(input_string)):
			if input_string[i] == "A":
				if input_string[i+1] == 'B':
					if input_string[i+2] == 'C':
						return True
					else:
						pass
				else:
					pass
			else:
				return False


print(findABC('AABCC'))
print(findABC('BEGABCE'))
print(findABC('BEAABCE'))
print(findABC('AACB'))
