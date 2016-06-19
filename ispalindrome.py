def is_palindrome(string):
	"""Return True/False if this word is a palindrome.
	Example::

	>>> is_palindrome("a")
	True

	>>> is_palindrome("noon")
	True

	>>> is_palindrome("racecar")
	True

	>>> is_palindrome("porcupine")
	False

	"""

	checker = list(string)[::-1]
	checker = ("").join(checker)
	return checker == string

	

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"