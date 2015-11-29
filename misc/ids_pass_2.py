"""
HEADER: Orbis ID checker by Lars Hedlund
@Description: Takes two files, a list of ids from orbis and list of ids from peoplesoft and
verifies that the ids match. If the ids are not in peoplesoft, it removes them
from the list in the final output. 
@Version: 0.0
"""
from sys import argv

# when running the program, the files need to be set ahead of time
# Ex: python ids_pass.py econ_ps.txt econ_or.txt econ_final.txt
script, peoplesoft, orbis, output, incorrect = argv

def id_check():
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