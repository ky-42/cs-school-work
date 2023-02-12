##
# Calculates the number of each type of rockTic that a citizen of bedrock
# will recive based on the weight of the rocks they bring to help build
# the rock hall
##

# Gets name of citizen and weight of rocks they brought
citizen_name = input("Please enter the citizen's name: ")
rocks_weight = round(float(input("Please enter the weight of the rocks: ")))

# Initializes variables to store the number of each type of ticket the citizen will get
a = 0
b = 0
c = 0

# Calculates number of tickets to be given
if rocks_weight <= 1000:
    c = 1
elif rocks_weight <= 3000:
    # Checks how many sets of 1000 pebbels of weight they brought without counting the first 1000 and sets it to b 
    b = (rocks_weight-1000) // 1000
    # Checks if there are any leftovers and if there are sets c to 2 otherswise sets c to 1
    c = 2 if ((rocks_weight/1000)%1) else 1
else:
    # Checks how many sets of 500 pebbels of weight they brought without counting the first 3000 and sets it to a 
    a = (rocks_weight - 3000) // 500
    b = 2
    # Checks if there are any leftovers and if there are sets c to 2 otherswise sets c to 1
    c = 2 if ((rocks_weight/500)%1) else 1

# Out puts tickets citizen should recive
print("%s you are eligible for the following rockTics..." % citizen_name.capitalize())
print("Type A rockTics: %s" % a)
print("Type B rockTics: %s" % b)
print("Type C rockTics: %s" % c)