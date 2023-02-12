##
# Helps track icebergs off the coast of Labrador
##

class Location:
    def __init__(self, r, c):
        self.__row = r
        self.__col = c

    def getRow(self):
        return self.__row

    def getCol(self):
        return self.__col

    def __repr__(self):
        return "(%d,%d)" % (self.__row, self.__col)

def printMap(locationList, mapRows, mapCols):
    theMap = []
    for i in range(mapRows):
        newRow = [" "]*mapCols
        theMap.append(newRow)
        
    for loc in locationList:
        theMap[loc.getRow()][loc.getCol()] = 'X'

    print("+"+"-"*mapCols+"+")
    for row in theMap:
        print("|",end="")
        for col in row:
            print(col,end="")
        print("|")
    print("+"+"-"*mapCols+"+")

# Returns data from log book in format (Grid size (str), start pos (str), pos changes (list[str]))) 
def readLogBook():
    # Opens and read logbook
    log_book = open("logbook.txt", "r")
    lines = log_book.readlines()
    log_book.close()

    return (lines[0], lines[1], lines[2:])

# Writes all the locations pass to a file of a passed name
def writeLoctions(locations, file_name):
    file = open(file_name, "w")
    for location in locations:
        file.write(f"({location.getRow()},{location.getCol()})\n")
    file.close()

# Returns a new location object give the currect position
# the new direction and position change amount
def moveIceburg(current, direction, change):
        if direction == "N":
            current[0] -= change
        elif direction == "S":
            current[0] += change
        elif direction == "E":
            current[1] += change
        elif direction == "W":
            current[1] -= change
        
        return Location(current[0], current[1])

def main():
    grid_dimensions, start, changes = readLogBook()

    # Changes the grind dimensions and current postion into the form [int, int]
    grid_dimensions = [int(i) for i in grid_dimensions.split(',')]
    current = [int(i) for i in start.split(',')]
    
    locations = [
        Location(current[0], current[1])
    ]
    
    for change in changes:
        # Splits position change into direction and change amount
        change = change.split(":")
        changeDirection = change[0]
        changeAmount = int(change[1])
            
        # Adds new location to location list
        locations.append(
            moveIceburg(current, changeDirection, changeAmount)
        )
    
    writeLoctions(locations, "locations.txt")

    printMap(locations, grid_dimensions[0], grid_dimensions[1])
            

if __name__ == "__main__":
    main()