def rev_list_in_place(lst):
    """Reverse list in place.
    Example::

	>>> rev_list_in_place([1, 2, 3])
	[3, 2, 1]
   
    """
    for i in range(len(lst) / 2):
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]

    return lst

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"