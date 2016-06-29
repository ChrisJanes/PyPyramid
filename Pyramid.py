""" Pyramid Generator

This module prints a right aligned pyramid of hashes to a specified height.
"""


def isInt(value):
	"""
	Checks if a given value is an integer or not

	:param value: The value to check
	:return: returns True if value is an int, False otherwise
	"""
	try:
		int(value)
		return True
	except:
		return False

def check_height(height):
	"""
	Validates the height of the pyramid requested by the user, performing bounds checking between 1 and 23

	:param height: The height value provided by the user
	:returns: the height value as an integer or -1
	"""
	if isInt(height) and int(height) > 0 and int(height) <= 23:
		return int(height)
	else:
		return -1

def build_line(line, height):
	"""
	Constructs the specified line for a pyramid of the given height

	:param line: the specific line to generate
	:param height: the overall height of the pyramid
	:return: returns a string constructed of a number of spaces and hash symbols
	"""
	hashCount = 2 + (line - 1)
	spaces = height - hashCount + 1
	output = "".ljust(spaces) + "".rjust(hashCount, "#")
	return output

def main():
	valid_input = False

	while valid_input == False:
		print "Enter the height of the pyramid: "
		in_height = raw_input()
		height = check_height(in_height)
		if height > -1:	
			valid_input = True
	print height

	for x in xrange(1,height+1):
		print build_line(x, height)

if __name__ == "__main__":
	main()