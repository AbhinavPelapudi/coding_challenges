
from collections import defaultdict

def is_anagram_of_palindrome(string):
	"""Is the word an anagram of a palindrome?

	Example::
	>>> is_anagram_of_palindrome("a")
	True

	>>> is_anagram_of_palindrome("ab")
	False

	>>> is_anagram_of_palindrome("aab")
	True

	>>> is_anagram_of_palindrome("arceace")
	True

	>>> is_anagram_of_palindrome("arceaceb")
	False

	"""

	letter_frequency = defaultdict(int)

	for letter in string: 
		letter_frequency[letter] += 1

	count = 0 
	for letter, f in letter_frequency.iteritems():
		if f % 2 == 1:
			count += 1 
		if count > 1:
			return False

	return True

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"











