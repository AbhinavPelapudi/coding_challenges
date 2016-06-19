def max_num(num_list):
	"""Returns largest integer from given list
	Example::

	>>> max_num([5, 3, 6, 2, 1])
	6

	"""

	highest_num = max(num_list)
	return highest_num


#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"