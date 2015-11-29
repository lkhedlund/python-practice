# this one is like argv scripts
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# that *args is pointless. Instead, just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."
	
print_two("Swedish", "Superstar")
print_two_again("Swedish", "Superstar")
print_one("Shotgun!")
print_none()