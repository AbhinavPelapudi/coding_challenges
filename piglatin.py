def pig_latin_word(phrase):
	"""Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.
    Example::


	>>> pig_latin_word('porcupine are cute')
	'orcupinepay areyay utecay'

	>>> pig_latin_word('give me an apple')
	'ivegay emay anyay appleyay'

    """
	pig_latinized = []
	vowels = ["a","e","i","o","u"]
	words = phrase.split(" ")
	for word in words:
		if word[0] in vowels:
			pig_latinized.append(word +"yay")
		else:
			pig_latinized.append(word[1:] + word[0] + "ay")

	return (" ").join(pig_latinized)

#####################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"