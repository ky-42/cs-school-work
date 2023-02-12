import random

##
# A two player game where each player takes turns picking a row in a 2D matrix
# then the computer generates a column giving the player a random position.
# Each position in the matrix has a number of gummies so the player will get
# the gummies in there random position and then there will be no gummies left
# in the positon. Player with the most gummies at the end of 5 turns wins.
##

# Given a number of rows and columns creates a 2D matrix with a random
# number of gummies between 50-99 in each position and returns the matrix
def createGameBoard(rows, columns):
    board = []
    for row in range(rows):
        row = []
        for column in range(columns):
            row.append(random.randint(50, 99))
        board.append(row)
    return board

# Creates a deep copy of a given 2D matrix (the game board) and returns it
def makeACopy(gameBoard):
    newCopy = []
    for row in gameBoard:
        newCopy.append(row[:])
    return newCopy

# Prints a formated version of the game board
def printBoard(gameBoard):
    for row in gameBoard:
        # String that will be formated in the print
        stringToFormat = "|" + ("{:<2}|"*len(row))
        # Adds all row elemets to the format method to format string
        formatedString = stringToFormat.format(*row)

        print(formatedString)

# Given the game board (A 2D matrix) lets each player pick a row 5 times
# then generates a random column and gets the value in the position in the 2D matrix.
# It adds the value in the position to the players collected gummies and sets the positon
# to a value of 0. Returns the players collected gummies in a list
# returns [player one gummies, player two gummies]
def collectGummies(gameBoard):
    collectedGummies = [0, 0]

    # Loops let each player play 5 times
    for _turn in range(5):
        for player in range(1, 3):
            playerRowIndex = int(input(f"Player {player}, enter your row number: (1-10)"))-1
            randomColumn = random.randint(0, 5)

            # Adds gummies in the position the player got to the players gummie count
            collectedGummies[player-1] += gameBoard[playerRowIndex][randomColumn]
            
            # Sets the position that the gummies was just retrived from to 0
            gameBoard[playerRowIndex][randomColumn] = 0

            print(f"Player {player}, your randomly chosen column is {randomColumn} so you get {collectedGummies[player-1]} gummy bears.")

    return collectedGummies

def main():
    playerOneName = input("Enter the name of player 1: ")
    playerTwoName = input("Enter the name of player 2: ")
    
    gameBoard = createGameBoard(10, 6)
    originalGameBoard = makeACopy(gameBoard)
    
    # Plays the game and gets scores
    scores = collectGummies(gameBoard)
    
    print()
    print("The Original Game Board:")
    printBoard(originalGameBoard)
    print()
    print("The Updated Game Board:")
    printBoard(gameBoard)
    print()

    print(f"{playerOneName} has {scores[0]} gummies.")
    print(f"{playerTwoName} has {scores[1]} gummies.")

    if scores[0] > scores[1]:
        print(f"{playerOneName} congratulations!!! You have won the game!")
    elif scores[0] < scores[1]:
        print(f"{playerTwoName} congratulations!!! You have won the game!")
    else:
        print("The game ended in a tie.")


if __name__ == "__main__":
    main()
