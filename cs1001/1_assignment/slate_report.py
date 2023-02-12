
##
# The program calculates how many materials are needed to create
# a report about past events for the people of tableland
##

# Constants for number of slates producable from differnt rock sizes
SLATES_IN_LARGE_ROCK = 500
SLATES_IN_SMALL_ROCK = 50

# Obtain number of reports needed and how many slates are in each report
slatesInReport = int(input("Enter the number of slates in a report: "))
numberOfReports = int(input("Enter the number of reports to be distributed: "))

# Calculates the number of slates needed to produce all the reports
slatesNeeded = slatesInReport * numberOfReports

# Calculates how many large rocks are needed to produce the reports with no extra slates
largeRocks = slatesNeeded // SLATES_IN_LARGE_ROCK
slatesNeeded -= largeRocks * SLATES_IN_LARGE_ROCK

# Calculates how many small rocks are needed to produce the remaining reports with no extra slates
smallRocks =  slatesNeeded // SLATES_IN_SMALL_ROCK
slatesNeeded -= smallRocks * SLATES_IN_SMALL_ROCK

# Outputs the materials needed 
print("Number of large rocks required is %i" % largeRocks)
print("Number of small rocks required is %i" % smallRocks)
print("Number of extra slates required is %i" % slatesNeeded)
