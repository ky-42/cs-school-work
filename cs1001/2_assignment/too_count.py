##
# Counts how many times "too" appears in several words
##

# Gets word to check for "too"
check_word = input('Please enter a word or Done to terminate the program: ')

while check_word != "Done":

    too_count = 0
    # Checks three letters behind this index for the word "too"
    current_index = 3
    while len(check_word) >= current_index:
        # Check if the three letters before the current index are equal to "too"
        if check_word[current_index-3:current_index] == "too":
            too_count += 1
        current_index += 1

    print(
        "too occurs %i times (s) in the word %s"
        % (too_count, check_word)
    )

    # Gets word to check for "too"
    check_word = input('Please enter a word or Done to terminate the program: ')

