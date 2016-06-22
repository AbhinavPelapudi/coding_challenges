import string
def decode(s):
	"""Decode a string.

	Example::
	>>> decode("0h")
	'h'

	>>> decode("2abh")
	'h'

	"""
	code = ""

	idx = 0 
	while idx < len(s):
		if s[idx] in string.digits:
			offset = int(s[idx]) + 1
			idx_letter = idx + offset
			letter = s[idx_letter]
			code += letter

		idx += 1

	return code


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"	
