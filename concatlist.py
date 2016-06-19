def concat_lists(list1, list2):
    """Combine lists.
    Example::
	>>> concat_lists([], [1, 2])
	[1, 2]

	>>> concat_lists([1, 2], [])
	[1, 2]

	>>> concat_lists([], [])
	[]

    """


    list3 = list1 + list2
    return list3

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"