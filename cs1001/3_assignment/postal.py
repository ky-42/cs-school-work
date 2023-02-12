##
# Orders a list of postal codes then prints them with codes starting with the same
# letter printed on the same line and the rest on separate lines
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
def mergeLists(values, low, middle, high):
    # Pointers for the start of the two virtual lists
    listOnePointer = low
    listTwoPointer = middle + 1

    # Sorts while the pointers have yet to reach the end of each list
    while (listOnePointer <= middle and listTwoPointer <= high):
        # If the value in the left list is already sorted remove it
        # from the virtual list
        if (values[listOnePointer] <= values[listTwoPointer]):
            listOnePointer += 1
        else:
            # Removes value from the right virtual list into the
            # sorted position 
            values.insert(listOnePointer, values.pop(listTwoPointer))
  
            # Moves pointers after part of the right list was removed
            middle += 1
            listOnePointer += 1
            listTwoPointer += 1


# Given a list of postal codes prints each one.
# prints postal codes that have to same starting letter
# in the same row if the list is sorted 
def printCodes(postalCodes):
    print("Sorted postal codes:", end="")
    # Letter to check to see if code should be in the same row as the last
    lastLetter = ""
    for code in postalCodes:
        # check if current code should be printed in the same row as last code
        if code[0] == lastLetter:
            print(code, end=" ")
        else:
            print("\n"+code, end=" ")
            lastLetter = code[0]
    print()

def main():
    postal_codes = ['A1A 1A1', 'B3K 5X5', 'V9A 7N2', 'A0Z 6P7', 'H0H 0H0', 'A1B 1T0']
    
    mergeSort(postal_codes, 0, len(postal_codes)-1)
    printCodes(postal_codes)

if __name__ == "__main__":
    main()