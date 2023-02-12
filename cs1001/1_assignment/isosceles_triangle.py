##
# Determines if 3 sticks of any length can form an isosceles triangle
##

# Gets the length of the three sticks
stickOne = float(input("Please enter the length of stick one: "))
stickTwo = float(input("Please enter the length of stick two: "))
stickThree = float(input("Please enter the length of stick three: "))

# Outputs first part of statment
print("You can", end=" ")

# Checks if you cant make a isosceles triangle if so add not to the output
if not (
    (stickOne == stickTwo) or
    (stickOne == stickThree) or
    (stickTwo == stickThree)
):
    print("not", end=" ")

# Outputs last part of statment
print("make an isosceles triangle.")
