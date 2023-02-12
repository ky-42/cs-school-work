##
# Takes a players name and a five letter word from the player
# then calculates a score for the word based on a set of given rules
# then compares the score with a generated computer score and delclares a winner
##

import random

# Gets players name and the five letter word for the game
player_name = input("Please enter your first name: ").lower().capitalize()
player_word = input("Please enter a five letter word: ")

# Adds all the ascii docimal codes for each letter of the word entered to the players score
player_score = 0
player_score += ord(player_word[0])
player_score += ord(player_word[1])
player_score += ord(player_word[2])
player_score += ord(player_word[3])
player_score += ord(player_word[4])

# Calculates the final player score
if not (player_score % 10):
    # Multiplies score by 5 if score is divisable by 5 and 10
    player_score *= 5
elif not ((player_score % 3) and (player_score % 7)):
    # Multiplies score by 3 if score is divisable by 3 or 7
    player_score *= 3
elif ((player_score % 8) and not (player_score % 2)):
    # Multiplies score by 2 if score is divisable by 2 and not by 8
    player_score *= 2

# Generates computers score
computer_score = random.randint(1500, 2000)

# Outputs player and computers score
print("%s your total points are %i" % (player_name, player_score))
print("The computer's total points are %i" % computer_score)

# Outputs if play won, lost, or tied
if player_score > computer_score:
    print("%s congratulations! You are the winner." % player_name)
elif player_score < computer_score:
    print("Sorry %s you have lost to the computer." % player_name)
else:
    print("%s you tied with with computer" % player_name)