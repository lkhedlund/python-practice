def findABC(input_string):
	if(len(input_string) < 3):
		return False
	else:
		for i in range(0, len(input_string), 1):
			if(i + 2 >= len(input_string)):
				return False
			else:
				temp_string = input_string[i] + input_string[i+1] + input_string[i+2]
				if(temp_string == 'ABC'):
					return True

		return False

print(findABC('AABCC'))