def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

	>>> show_evens([1, 2, 3, 4, 6, 8])
	[1, 3, 4, 5]

    """
    even_index_nums = []
    for i in range(len(nums)):
    	if nums[i] % 2 == 0:
    		even_index_nums.append(i)

    return even_index_nums


#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"