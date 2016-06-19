def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    # assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    max = 100
    min = 0

    while True:
        checker = (max-min)/2 + min #checker=50
        num_guesses+=1
        
        if val < checker:
            max = checker
           

        elif val > checker:
            min = checker
            # print min

        elif val == checker:
            break

    return num_guesses

# print binary_search(50)
# print binary_search(25)
print binary_search(75)