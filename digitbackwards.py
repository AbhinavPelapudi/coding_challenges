def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

    Example::

    >>> print_digits(1)
	1

	>>> print_digits(314)
	4
	1
	3

	>>> print_digits(12)
	2
	1

    """
    num_length = len(str(num))
    number = num
    count = 0 
    while count < num_length:
    	num_to_print = number % 10 
    	print num_to_print
    	count += 1
    	number = number / 10
    	 



#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"


