##
# Takes positive decimal numbers from user and converts them to hex
##

def main():
    # Gets a decimal value from user and passes it to decToHex
    # and prints the return value while input is not equal to 0
    decimal_number = int(input("Enter a decimal value, 0 to finish: "))
    while decimal_number != 0:
        print(decToHex(decimal_number))
        decimal_number = int(input("Enter a decimal value, 0 to finish: "))

# Converts decimal value to hex
# dec_value = decimal value to convert
# returns string containing the decimal value converted to hex
def decToHex(dec_value):
    hex_string = ""
    # Uses a mathmatical fomula to compute hex values refer to assignment handout
    while dec_value != 0:
        # Adds new char to hex string
        hex_string = getHexChar(dec_value%16) + hex_string
        dec_value = dec_value//16
    return hex_string

# Gets a single hex digit from a decimal value between 0-16
# dec_digit = decimal digits to convert
# Returns string of hex digit
def getHexChar(dec_digit):
    if dec_digit > 9:
        # If the hex digit is a letter gets the letter by looking up to passed digits plus 55 in ascii
        return chr(55+dec_digit)
    # Returns digits passed as a string if they stay the same
    return str(dec_digit)

if __name__ == "__main__":
    main()