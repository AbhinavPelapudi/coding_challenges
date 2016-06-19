import random

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
    Example::


	>>> lucky_numbers(0)
	[]

	>>> sorted(lucky_numbers(10))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    """

    numbers = [1,2,3,4,5,6,7,8,9,10]
    lucky_nums = set()

    while True:
    	if len(lucky_nums) == n:
    		break
    	found_num = random.choice(numbers)
    	lucky_nums.add(found_num)

    lucky_nums = list(lucky_nums)
    return lucky_nums





#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"