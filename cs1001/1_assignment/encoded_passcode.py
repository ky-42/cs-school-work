##
# Decodes the passcode that opens the magical door on the tower that repunzel is traped in
##

# Obtain the words outside the tower that will be decoded to the passcode
firstWord = input("Please enter the first word: ")
secondWord = input("Please enter the second word: ")
thirdWord = input("Please enter the third word: ")

# Gets first letter from first word
firstLetter = firstWord[0]

# Gets the middle letter from the second word
secondLetter = secondWord[len(secondWord)//2]

# Gets the last letter of the third word (Not including the number at the end)
thirdLetter = thirdWord[-2]

# Gets number at end of third word
numberOfTimes = int(thirdWord[-1])

# Concatenates all the letters to make the full word used in the passcode
passcodeWord = firstLetter + secondLetter + thirdLetter

# Repeats the word in the passcode by the number of times it needs to be said
passcode = passcodeWord*numberOfTimes

# Outputs the decoded passcode
print("To open the magical door of the tower say %s into the peep hole under the window." % passcode)
