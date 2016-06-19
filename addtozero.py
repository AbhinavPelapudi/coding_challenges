def add_to_zero(nums):
	"""Given list of ints, return True if any two nums in list sum to 0.
	Example::
		>>> add_to_zero([])
		False

		>>> add_to_zero([1])
		False

		>>> add_to_zero([1, 2, 3])
		False

		>>> add_to_zero([1, 2, 3, -2])
		True"""

	flag = False
	if nums == []:
		return False
	if len(nums) == 1:
		return False

	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			if nums[i] + nums[j] == 0:
				flag = True
	return flag
			


#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
   