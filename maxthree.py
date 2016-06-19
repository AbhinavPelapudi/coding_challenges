def max_of_three(num1,num2,num3):
	"""Returns the largest of three integers
	Example::

	>>> max_of_three(1, 5, 2)
	5

	>>> max_of_three(10, 1, 11)
	11

	"""

	greatest = num1
	if num2 > greatest:
		greatest = num2
	if num3 > greatest:
		greatest = num3

	return greatest

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"