##
# Computes and prints the range of ratings for a shuttle type.
# Also computes and prints the average rating for each shuttle maker
# excluding there lowest rating.
##

# Given a 2D matrix and column index return a column from the 2D matrix
def getColumn(matrix, columnIndex):
    column = []
    for row in matrix:
        column.append(row[columnIndex])
    return column

# Given a 2D matrix of ratings and a list of the shuttle type names
# computes and prints the range for each type of shuttle (matrix row)
def computeAllRanges(shuttleTypes, ratings):
    print("{:<20} {:<20}".format('Shuttle Types', 'Range of Ratings'))

    # Loops over each shuttle types ratings
    for shuttleTypeIndex in range(len(ratings)):
        ratingRange = max(ratings[shuttleTypeIndex]) - min(ratings[shuttleTypeIndex])
        print("{:<20} {:<20.2f}".format(shuttleTypes[shuttleTypeIndex], ratingRange))

# Given the ratings table and the column to check computes
# the average rating in the column not including the lowest rating
# then returns the average
def computeAverage(ratings, columnNumber):
    # Gets all the shuttle makers ratings
    columnRatings = getColumn(ratings, columnNumber)

    # Removes the lowest rating from the column
    lowestRating = min(columnRatings)
    columnRatings.remove(lowestRating)

    # Computes the average without the lowest rating and returns it
    averageRating = sum(columnRatings)/len(columnRatings)
    return averageRating

def main():
    shuttleTypes = ["Racer", "Everyday", "Emergency", "Heavy Duty", "Light"]
    shuttleMakers = ["Jupishut", "Shuttlejup", "Shuttlesrjup", "Jupnride", "Riderjup", "Shuttlejrides", "Shuttajup"]
    ratings = [
        [80,90,55,65,80,65,70],
        [65,45,85,80,80,80,75],
        [90,60,90,90,40,45,75],
        [75,55,95,95,65,95,90],
        [80,90,75,65,75,60,80]
    ]

    computeAllRanges(shuttleTypes, ratings)
    
    print()

    # All under for computing and printing average rating for each shuttle maker
    print("{:<20} {:<20}".format('Shuttle Maker', 'Average Rating'))
    # Loops over each shuttle maker
    for shuttleMakerIndex in range(len(shuttleMakers)):
        averageRating = computeAverage(ratings, shuttleMakerIndex)
        print("{:<20} {:<20.2f}".format(shuttleMakers[shuttleMakerIndex], averageRating))

if __name__ == "__main__":
    main()