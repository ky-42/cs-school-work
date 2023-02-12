##
# Calculates the square tabft of materials needed to create a tabuline (house) with specific specifications in tableland.
# Also Calculates the cost to build said tabuline.
##

# Constant for cost of materials per square tabft
COST_PER_SQUEARE_TABFT = 50

# Gets the specifications of the tabuline
numberOfSides = int(input("Please enter the number of sides for the regular polygon: "))
lengthOfSide = float(input("Please enter the length of a side of the regular polygon: "))
lengthOfApothem = float(input("Please enter the length of the apothem of the regular polygon: "))
heightOfTabuline = float(input("Please enter the height of the tabuline: "))

# Calculates the perimeter of the tabuline
tabulinePerimeter = numberOfSides*lengthOfSide

# Calculates the area of the roof and the floor of the tabuline
roofAndFloorArea = lengthOfApothem*tabulinePerimeter

# Calculates the area of all the sides of the house combined
allSidesArea = lengthOfSide*heightOfTabuline*numberOfSides

# Calculates the total square tabft of materals needed to create the tabuline
totalArea = roofAndFloorArea+allSidesArea

# Calculates the cost of all the materials needed
totalCost = totalArea*COST_PER_SQUEARE_TABFT

# Outputs the total square tabft and the cost of the materials
print("The cost to build the %.2f square tabft tabuline is %.2f tably." % (totalArea, totalCost))


