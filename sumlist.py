def sum_list(num_list):

    """Return the sum of all numbers in list.
    Example::

	>>> sum_list([5, 3, 6, 2, 1])
	17

    """
    sum_num = 0 
    for num in num_list:
    	sum_num += num

    return sum_num

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"