
def fizzbuzz():
	"""Count from 1 to 20 in fizzbuzz fashion.
	Example:: 

	>>> fizzbuzz()
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	17
	fizz
	19
	buzz

	"""
	for num in range(1,21):
		if num % 15 == 0:
			print "fizzbuzz"
		elif num % 5 == 0:
			print "buzz"
		elif num % 3 == 0:
			print "fizz"
		else: 
			print num

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"