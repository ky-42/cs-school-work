##
# Outputs the number of days in a month given the month
##

# Gets month from user
month = input("Please enter a month: ").lower().strip()

if (
    # Checks if month entered is a month with 31 days
    month == "january" or
    month == "march" or
    month == "may" or
    month == "july" or
    month == "august" or
    month == "october" or 
    month == "december"
):
    print("%s has 31 days." % month.capitalize())
elif (
    # Checks if month entered is a month with 30 days
    month == "april" or
    month == "june" or
    month == "september" or
    month == "november"
):
    print("%s has 30 days." % month.capitalize())
elif month == "february":
    print("February has 28 or 29 days.")
else:
    print("Incorrect month name entered")
