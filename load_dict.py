"""
Loads a text file as a list 

Arguments:
- file name and directory 

Exceptions:
- IO error if not found 

Returns:
- list containing all of the words in lower case

Requires:
- import sys
"""
import sys


def open_file(file):
	try:
		with open(file) as in_file:
			loaded_txt = in_file.read().strip().split('\n')
			loaded_txt = [x.lower() for x in loaded_txt]
			return loaded_txt
	except IOError as e:
		print("{}\nError Opening {}. Terminating" .format(e,file))
		sys.exit(1)