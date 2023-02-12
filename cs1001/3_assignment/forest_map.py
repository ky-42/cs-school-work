##
# Given a forest layout (2D matrix) checks if Hansel and Gretel will
# have enough breadcrumbs (Amount entered by user) to move though
# the forests open spaces (moving only south and east) leaving a
# breadcrumb at each position.
##

# Given the forest layout and the inital breadcrumbs checks how many
# breadcrumbs will be left after going from the top left to the bottom
# right leaving a breadcrumb in every position. Returns the number of breadcrumbs left
def distance(forestLayout, initialBreadcrumbs):
    # The column to start at in the next itteration of the second for loop
    minColumn = 0
    for row in range(len(forestLayout)):
        # Goes though each column in the row starting where the last row left off
        # till it reaches a tree then moves to the next row till at bottom right
        for column in range(minColumn, len(forestLayout[row])):
            if forestLayout[row][column] == "E":
                # If in bottom right return the number of breadcrumbs left
                return initialBreadcrumbs
            elif forestLayout[row][column] == " ":
                # Leaves a breadcrumb in current position if there are any left
                if initialBreadcrumbs > 0:
                    forestLayout[row][column] = "*"
                initialBreadcrumbs -= 1
                # Sets column to start at in next row
                minColumn = column
            else:
                # move to next row if there is a tree in current position
                break

# Given a number of breadcrumbs left after the trip prints whether there
# were enough for the trip
def crumbsLeft(breadcrumbsLeft):
    if breadcrumbsLeft < 0:
        print("Not enough breadcrumbs for the trip.")
    elif breadcrumbsLeft == 0:
        print("Phew, just enough breadcrumbs for the trip.")
    else:
        print(f"{breadcrumbsLeft} breadcrumb(s) are left.")

def main():
    forestPath = [
        [' ',' ',' ','X','X'],
        ['X','X',' ',' ','X'],
        ['X','X','X',' ','X'],
        [' ','X','X',' ',' '],
        [' ','X','X','X',' '],
        [' ',' ','X','X',' '],
        [' ',' ','X','X','E']
    ]

    breadcrumbs = int(input("Enter number of breadcrumbs: "))
    
    breadcrumbsLeft = distance(forestPath, breadcrumbs)
    print(crumbsLeft(breadcrumbsLeft))

    print(forestPath)


if __name__ == "__main__":
    main()