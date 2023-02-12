##
# Given a list of laureates prints a sorted list of how many laureates where
# won in each area in order
##

# Implmentation of inplace merge sort
# Pass list to sort and the indexes of the start and end
# of a virtual list to sort
def mergeSort(values, low, high):
    if low == high: return

    # Splits virtual list in two then sorts and merges both virtual lists
    middle = (low+high)//2
    mergeSort(values, low, middle)
    mergeSort(values, middle+1, high)
    mergeLists(values, low, middle, high)

# Merges two virtual sorted lists that are next to each other into a
# single virtual sorted list. Should be given the lowest index of 
# the first virtual list. the middle index of the two lists and the highest
# index of the second list
# IMPORTANT List passed must be in form [(name, number), ...]
def mergeLists(values, low, middle, high):
    # Pointers for the start of the two virtual lists
    listOnePointer = low
    listTwoPointer = middle + 1

    # Sorts while the pointers have yet to reach the end of each list
    while (listOnePointer <= middle and listTwoPointer <= high):
        # If the value in the left list is already sorted remove it
        # from the virtual list
        if (values[listOnePointer][1] > values[listTwoPointer][1]):
            listOnePointer += 1
        else:
            # If the number of laureats in the area was the same 
            # switches to ordering by area name
            if (values[listOnePointer][1] == values[listTwoPointer][1]):
                # If the name is already sorted remove it
                # from the left virtual list. Other wise just let the code to remove
                # from the right list run
                if (values[listOnePointer][0] < values[listTwoPointer][0]):
                    listOnePointer +=1
                    continue

            values.insert(listOnePointer, values.pop(listTwoPointer))
            middle += 1
            listOnePointer += 1
            listTwoPointer += 1

# Given a list of areas and a list of laureates creates a
# list in the form [(area, amount won), ...] and returns it
def count(areasList, laureatesList):
    # Creates a list of zeros and each zero is the count for a coresponsing area
    countList = [0]*len(areasList)
    for laureate in laureatesList:
        # Gets the index in the area list of the current laureats area
        areaIndex = areasList.index(laureate[2])
        # Adds 1 to the value in the count list based on the index gotten above
        countList[areaIndex] += 1
    # Combines each value in the areas list with one in the count list
    # in the order they show up 
    areasCount = list(zip(areasList, countList))
    return areasCount

# Prints a formated list of the number of laureates
# in each area given a list in the form of [(area, amount won), ...]
def printList(areasCount):
    for area in areasCount:
        print("{:>30} {}".format(area[0], area[1]))

# Sorts the list in the form [(area, amount won), ...]
def sortByAmount(areasCount):
    mergeSort(areasCount, 0, len(areasCount)-1)    

def main():
    nobelAreas = ["Chemistry","Physics","Literature","Peace","Economics", "Physiology or Medicine"]
    nobelWinners = [
        ["Albert Einstein",1921,"Physics"],
        ["Marie Curie",1903,"Physics"],
        ["Bertrand Russell",1950,"Literature"],
        ["Barbara McClintock",1983,"Physiology or Medicine"],
        ["Nelson Mandela",1993,"Peace"],
        ["Marie Curie",1911,"Chemistry"],
        ["Amartya Sen",1998,"Economics"]
    ] 
    
    areasCount = count(nobelAreas, nobelWinners)
    sortByAmount(areasCount)
    printList(areasCount)

if __name__ == "__main__":
    main()