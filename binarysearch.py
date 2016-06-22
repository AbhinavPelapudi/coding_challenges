def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    Example::
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    """

    num_guesses = 0

    max = 100
    min = 0

    while True:
        checker = (max - min) / 2 + min 
        num_guesses += 1
        
        if val < checker:
            max = checker

        elif val > checker:
            min = checker
          
        else:
            break

    return num_guesses

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"

