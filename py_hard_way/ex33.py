

numbers = []

def whileHelp(end, inc):
	i = 0
	while i < end:
		print "At the top of i is %d" % i
		numbers.append(i)
	
		i = i + inc
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

whileHelp(int(raw_input("End > ")), int(raw_input("Increment > ")))

print "The numbers: "

for num in numbers:
	print num