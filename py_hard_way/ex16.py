# HEADER DOCUMENTATION: This is a simple text editor that will erase a file's current 
# contents and replace it with three lines. 

# Version: 0.1
# Program features: (1)erase file, (2)save file

from sys import argv

# User will need to provide the script name and file name in the command line. 
script, filename = argv

# Erases the contents of the file. 
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()