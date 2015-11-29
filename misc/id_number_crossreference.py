from sys import argv

script, ids_peoplesoft, ids_orbis, output_file = argv

def check_ids():
	"""
	@input: none
	@return: none
	Function references a list of id numbers in peoplesoft against orbis
	and writes the id numbers into a new file if they are present.
	"""
	with open(ids_peoplesoft, 'r') as file1:
		with open(ids_orbis, 'r') as file2:
			same = set(file1).intersection(file2)
			
	same.discard('\n')
	
	with open(output_file, 'w') as file_out:
		for line in same:
			file_out.write(line)
			
check_ids()