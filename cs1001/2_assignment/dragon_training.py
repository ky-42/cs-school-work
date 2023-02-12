##
# Checks if a young viking is qualified to hav a dragon under their control
##

# Gets the number of participants to know how many times to execute the loop 
number_of_participants = int(input('Please enter the number of participants: '))

for _ in range(number_of_participants):
    # Gets participants name and score
    participant_name = input('Please enter the name of the participant: ')
    participant_score = float(input('Please enter the total points: '))
    
    # Checks if participants score if between 30 and 50 if so
    # outputs that they passed and what their score was
    if 50 >= participant_score >= 30:
        print(
            '%s passed the training with %.2f points.'
            % (participant_name.capitalize(), participant_score)
        )