# encryption using a linear feedback shift register
import bindec

# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c: str) -> list:
    if c.isupper():
        return bindec.decToBin(ord(c)-65)
    elif c.islower():
        return bindec.decToBin(ord(c)-71)
    elif c.isdigit():
        return bindec.decToBin(ord(c)+4)
    elif c == "+":
        return bindec.decToBin(62)
    elif c == "/":
        return bindec.decToBin(63)
    return []

# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b: str) -> str:
    char_decimal = bindec.binToDec(b)
    if char_decimal < 26:
        return chr(char_decimal + 65)
    elif char_decimal < 52:
        return chr(char_decimal + 71)
    elif char_decimal < 62:
        return chr(char_decimal - 4)
    elif char_decimal == 62:
        return chr(char_decimal - 19)
    elif char_decimal == 63:
        return chr(char_decimal - 16)
    return ""

# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(s: str) -> list:

    string_bin = []

    for char in s:
        string_bin.extend(charToBin(char))

    return string_bin

# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list: list) -> str:

    bin_string = ''

    for index_bot in range(0, len(b_list), 6):
        # Splits bit list into 6 bits then gets char
        bin_string += binToChar(b_list[index_bot:index_bot+6])        

    return bin_string

# generates a sequence of pseudo-random numbers
def generatePad(seed: list, k: int, length: int) -> list:
    
    seed_len = len(seed)
    pad = []
    
    while len(pad) < length:
        rand_num = seed[0] ^ seed[seed_len-k]
        pad.append(rand_num)
        
        # Shifts bits in seed 
        seed.append(rand_num)
        del seed[0]
    
    return pad


# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message: str, seed: list, k: int) -> str:
    
    bin_message = strToBin(message)
    pad = generatePad(seed, k, len(bin_message))
    encrypted_message = []

    # Encrypts message
    for bin_index in range(len(bin_message)):
        encrypted_message.append(pad[bin_index] ^  bin_message[bin_index])

    return binToStr(encrypted_message)
