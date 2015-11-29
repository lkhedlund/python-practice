# imports argv
from sys import argv

# tells python what arguments it takes in the command line
script, input_file = argv

# creates a function that prints the file passed in the command line and reads it.
def print_all(f):
	print f.read()
	
# 'rewinds' the file by placing the cursor at the beginning, i.e. seek 0.
def rewind(f):
	f.seek(0)

# creates a function that print the line count and then the line. 
def print_a_line(line_count, f):
	print line_count, f.readline()

# sets the file as the one passed in the command
current_file = open(input_file)
	
print "First let's print the whole file:\n"

# prints the entire file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# sets the file back to "0"
rewind(current_file)

print "Let's print three lines:"

# each line prints and adds one to the count.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)