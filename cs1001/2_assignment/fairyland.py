##
# Gets names of fairys participating in the fly high game
# and generates what colour dust they were dusted in and 
# how high they flew. After all the fairys have been entered
# prints the name of the participant that flew the highest
# also prints how high they flew.
##

import random

def main():
    
    # Used to store data about highest flyer
    top_height = 0
    top_participant_name = ""
    
    fary_name = input("Enter a fairy's name, 'end' when done: ")

    
    while fary_name != "end":
        # Generates current fairys dust colour and height
        participant_colour = pixieDusting()
        participant_height = computeHeight(participant_colour)

        print(
            "%s was dusted with %s pixie dust and flew %i metres high."
            % (fary_name, participant_colour, participant_height)
        )
        
        # Sets the data about the highest flyer to the current fairy
        # if the current fairy set the hight record
        if participant_height > top_height:
            top_height = participant_height
            top_participant_name = fary_name

        fary_name = input("Enter a fairy's name, 'end' when done: ")
    
    print(
        "The highest flight was %i by %s"
        % (top_height, top_participant_name)
    )
        
# returns a random colour 
# Possible colours are Red, Greed, Blue, Yellow
def pixieDusting():
    return random.choice((
        "Red",
        "Green",
        "Blue",
        "Yellow"
    ))    

# Generates a random height based on colour passed
# colour = colour of dust fairy has been dusted in
# returns a random number between a range determined by the colour passed
def computeHeight(colour):
    if colour == "Red":
        return random.randint(40, 49)
    elif colour == "Blue":
        return random.randint(30, 39)
    elif colour == "Green":
        return random.randint(20, 29)
    else:
        return random.randint(10, 19)

if __name__ == "__main__":
    main()