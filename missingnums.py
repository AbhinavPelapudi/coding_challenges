def missing_number(lst, max_num):
	"""Find the missing number in a list
	Example::

	>>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
	8

	"""


	sorted_set = sorted(lst)
	if sorted_set[0] != 1:
		return 1
	if sorted_set[-1] != max_num:
		return max_num

	missing_num = None

	idx = 0 
	while idx < len(sorted_set) - 1:
		if sorted_set[idx] != sorted_set[idx + 1] - 1:
			missing_num = sorted_set[idx] + 1

		idx += 1

	return missing_num




#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
		