##
# A two player number guessing game where you play a number of "sets" 
# which is determined by the users. Both players have two attempts to 
# guess a random number in each set and get points depending on when and 
# if they guess it. The player with the most points a the end wins.
##

import random

def main():
    sets_to_play = int(input("Please enter the number of sets you wish to play: "))
    
    # List in format [Player name, Player score]
    player_one_name_score = [input("Please enter first player's name: "), 0]
    player_two_name_score = [input("Please enter second player's name: "), 0]

    for set_num in range(1, sets_to_play+1):
        
        # Generates a random number for each player to guess
        player_one_rand_num = random.randint(1, 6)
        player_two_rand_num = random.randint(1, 6)
        
        # Gets the points each player earned this set
        player_one_points = computePoints(player_one_name_score[0], player_one_rand_num)
        player_two_points = computePoints(player_two_name_score[0], player_two_rand_num)

        # Prints each players score from this set
        print("\nFor SET %i:" % set_num)
        print(
            "%s, has earned %i points. The random number was: %i"
            % (player_one_name_score[0], player_one_points, player_one_rand_num)
        )
        print(
            "%s, has earned %i points. The random number was: %i"
            % (player_two_name_score[0], player_two_points, player_two_rand_num),
            end="\n\n"
        )
        
        # Adds points from this set to players overall score
        player_one_name_score[1] += player_one_points
        player_two_name_score[1] += player_two_points
    
    printWinner(player_one_name_score, player_two_name_score)

# Lets players guess the random number and returns the points the player recived
# Params are the name of the player and the random number they are trying to guessing
def computePoints(name, rand_num):
    guess_one = int(input("%s, enter your first guess: " % name))
    if guess_one == rand_num:
        return 5

    guess_two = int(input("%s, enter your second guess: " % name))
    if guess_two == rand_num:
        return 3

    return 0

# Determines who won the game and prints their name
# Two params are the data for player one and player two in format
# [Player name, Player score]
def printWinner(player_one_name_score, player_two_name_score):
    if player_one_name_score[1] > player_two_name_score[1]:
        print("%s is the winner of the game." % player_one_name_score[0])
    elif player_one_name_score[1] < player_two_name_score[1]:
        print("%s is the winner of the game." % player_two_name_score[0])
    else:
        print("The game ended in a draw.")
    
if __name__ == "__main__":
    main()