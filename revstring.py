def rev_string(astring):
    """Return reverse of string.
    Example::
    >>> rev_string('apple')
	'elppa'

    """

    return astring[::-1]

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"