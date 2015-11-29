"""
HEADER: PASS Orbis ID checker by Lars Hedlund
@Description: Takes two files, a list of ids from orbis and list of ids from peoplesoft and
verifies that the ids match. If the ids are not in peoplesoft, it removes them
from the list in the final output. 
@Version: 0.1
"""
from sys import exit

def id_check():
	orbis = filename_import("orbis")
	peoplesoft = filename_import("peoplesoft")
	output = filename_import("output")
	#opens the orbis id numbers and reads through each line
	with open(orbis, 'r') as f1:
		orbis_ids = f1.readlines()

	#opens the peoplesoft id numbers and reads through each line
	with open(peoplesoft, 'r') as f2:
		peoplesoft_ids = f2.readlines()
	
	with open(output, 'w+') as o1: #opens output file
		for id in orbis_ids: #loops through each id in orbis
			if id in peoplesoft_ids: #if the id is in the peoplesoft list
				o1.write(id) #writes the id to the output
			else:
				pass #if not, skips over it.

def filename_import(name):
	#input(string, string)
	#returns(string)
	correct_name = False
	while correct_name == False:
		print "Please enter the file name for the %s file." % name
		filename = raw_input("Ex: econ_%s.txt >>> " % name) 
		if ".txt" in filename:
			return filename
			correct_name = True
		else:
			print "Please enter a .txt file only."
		
def main():	
	print """
=====================================================================
PASS Orbis ID Validator by Lars Hedlund
=====================================================================
This program takes a list of ID numbers from orbis events and checks
them against a list of valid ID numbers from peoplesoft.
The program prints all ID numbers that are valid into a new output
file, which can be used to determine attendance Y/N and number of 
sessions attended in the final SPSS analysis. 

NOTE: The orbis, peoplesoft, and export files MUST be in the same
directory as this program, and must be .txt files.
	"""
	print "Do you want to proceed?"
	continue_run = raw_input("If yes, type 'Y'. If not, press any key to exit >>> ")
	if continue_run in "Yy":
		id_check()
		print "Copying Complete."
	else:
		exit(0)
		
main()