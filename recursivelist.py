def print_recursively(lst):
    """Print items in the list, using recursion.

    Example::

    >>> print_recursively([1, 2, 3])
	1
	2
	3

    """
     
    if lst:
    	print lst[0]
    	print_recursively(lst[1:])
    

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"



