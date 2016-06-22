def count_recursively(lst):
	"""Return number of items in a list, using recursion.
	Example::

	>>> count_recursively([])
	0

	>>> count_recursively([1, 2, 3])
	3

	"""
	if lst == []:
		return 0 

	
	return  count_recursively(lst[1:]) + 1


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"	
	