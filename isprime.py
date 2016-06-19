def is_prime(num):
	"""Is a number a prime number?
	Example::

	>>> is_prime(2)
	True

	>>> is_prime(3)
	True

	>>> is_prime(4)
	False

	>>> is_prime(11)
	True

	>>> is_prime(999)
	False
	"""

	if num == 2:
		return True

	for factorial in range(2,num):
		if num % factorial == 0:
			return False
		
	return True



#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"