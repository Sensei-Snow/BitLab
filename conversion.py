#------------------------------------------------------------------------------------Verify
def verify_decimal(integer):
    str_value = str(integer)
    if all(char in "0123456789" for char in str_value) and str_value != '':
        return True

def verify_binary(string):
    if all(char in "01b" + ' ' for char in string) and string != '':
        return True

def verify_hexadecimal(string):
    if all(char in "0123456789abcdefABCDEFx" + ' ' for char in string) and string != '':
        return True

def verify_char(value):
    if len(value) == 1 and 0 <= ord(value) <= 255 and value != '':
        return True

def verify_string(string):
    if string != '':
        return True

#------------------------------------------------------------------------------------Decimal to...
def decimal_to_binary(string):
    if verify_decimal(string):
        integer = int(string)
        binary = bin(integer)[2:]

        if len(binary)%8!=0:
            additional_zero = '0' * (8-len(binary)%8)
            additional_zero += binary
        else:
            return binary

        if len(additional_zero)>8:
            binary_space = ' '.join(additional_zero[i:i+8] for i in range(0, len(additional_zero), 8))
            return binary_space
        else:
            return additional_zero
    else:
        return "[ERROR] -- Invalid decimal value"

def decimal_to_hexadecimal(string):
    if verify_decimal(string):
        integer = int(string)
        hexadecimal = hex(integer)[2:]

        if len(hexadecimal)%2!=0:
            additional_zero = '0' * (2-len(hexadecimal)%2)
            additional_zero += hexadecimal
        else:
            return hexadecimal.upper()

        if len(additional_zero)>2:
            hexadecimal_space = ' '.join(additional_zero[i:i+2] for i in range(0, len(additional_zero), 2))
            return hexadecimal_space.upper()
        else:
            return additional_zero.upper()
    else:
        return "[ERROR] -- Invalid decimal value"

def decimal_to_char(integer):
    if verify_decimal(integer):
        if integer < 0 or integer > 255:
            return "[ERROR] -- Invalid decimal value"
        else:
            return chr(integer)
    else:
        return "[ERROR] -- Invalid decimal value"

def decimal_to_string(string):
    if verify_decimal(string):
        decimal_list = string.split()
        char_list = []
        for decimal in decimal_list:
            char_list.append(decimal_to_char(int(decimal)))
        return ''.join(char_list)
    else:
        return "[ERROR] -- Invalid decimal value"

#------------------------------------------------------------------------------------Binary to...
def clean_binary(string):
    binary_clean1 = string.replace(' ', '')
    return binary_clean1.replace('0b', '')

def binary_to_decimal(string):
    if verify_binary(string):
        binary_clean = clean_binary(string)
        return int(binary_clean, 2)
    else:
        return "[ERROR] -- Invalid binary value"

def binary_to_hexadecimal(string):
    if verify_binary(string):
        binary_clean = clean_binary(string)
        decimal = binary_to_decimal(binary_clean)
        return decimal_to_hexadecimal(decimal)
    else:
        return "[ERROR] -- Invalid binary value"

def binary_to_char(string):
    if verify_binary(string):
        binary_clean = clean_binary(string)
        decimal = binary_to_decimal(binary_clean)
        if decimal < 0 or decimal > 255:
            return "[ERROR] -- Invalid binary value"
        else:
            return decimal_to_char(decimal)
    else:
        return "[ERROR] -- Invalid binary value"

def binary_to_string(string):
    if verify_binary(string):
        binary_list = string.split()
        char_list = []
        for binary in binary_list:
            char_list.append(binary_to_char(binary))
        return ''.join(char_list)
    else:
        return "[ERROR] -- Invalid binary value"

#------------------------------------------------------------------------------------Hexadecimal to...
def clean_hexadecimal(string):
    hexadecimal_clean1 = string.replace(' ', '')
    return hexadecimal_clean1.replace('0x', '')

def hexadecimal_to_decimal(string):
    if verify_hexadecimal(string):
        hexadecimal_clean = clean_hexadecimal(string)
        return int(hexadecimal_clean, 16)
    else:
        return "[ERROR] -- Invalid hexadecimal value"

def hexadecimal_to_binary(string):
    if verify_hexadecimal(string):
        hexadecimal_clean = clean_hexadecimal(string)
        decimal = hexadecimal_to_decimal(hexadecimal_clean)
        return decimal_to_binary(decimal)
    else:
        return "[ERROR] -- Invalid hexadecimal value"

def hexadecimal_to_char(string):
    if verify_hexadecimal(string):
        hexadecimal_clean = clean_hexadecimal(string)
        decimal = hexadecimal_to_decimal(hexadecimal_clean)
        if decimal < 0 or decimal > 255:
            return "[ERROR] -- Invalid hexadecimal value"
        else:
            return decimal_to_char(decimal)
    else:
        return "[ERROR] -- Invalid hexadecimal value"

def hexadecimal_to_string(string):
    if verify_hexadecimal(string):
        hexadecimal_list = string.split()
        char_list = []
        for hexadecimal in hexadecimal_list:
            char_list.append(hexadecimal_to_char(hexadecimal))
        return ''.join(char_list)
    else:
        return "[ERROR] -- Invalid hexadecimal value"

#------------------------------------------------------------------------------------Char to...
def char_to_decimal(char):
    if verify_char(char):
        return ord(char)
    else:
        return "[ERROR] -- Invalid character value"

def char_to_binary(char):
    if verify_char(char):
        decimal = char_to_decimal(char)
        return decimal_to_binary(decimal)
    else:
        return "[ERROR] -- Invalid character value"

def char_to_hexadecimal(char):
    if verify_char(char):
        decimal = char_to_decimal(char)
        return decimal_to_hexadecimal(decimal)
    else:
        return "[ERROR] -- Invalid character value"

#------------------------------------------------------------------------------------String to...
def string_to_decimal(string):
    if verify_string(string):
        char_list = list(string)
        decimal_list = []
        for char in char_list:
            decimal_list.append(char_to_decimal(char))
        return ' '.join(str(decimal) for decimal in decimal_list)
    else:
        return "[ERROR] -- Invalid string value"

def string_to_binary(string):
    if verify_string(string):
        char_list = list(string)
        decimal_list = []
        binary_list = []
        for char in char_list:
            decimal_list.append(char_to_decimal(char))
        for decimal in decimal_list:
            binary_list.append(decimal_to_binary(decimal))
        return ' '.join(str(binary) for binary in binary_list)
    else:
        return "[ERROR] -- Invalid string value"

def string_to_hexadecimal(string):
    if verify_string(string):
        char_list = list(string)
        decimal_list = []
        hexadecimal_list = []
        for char in char_list:
            decimal_list.append(char_to_decimal(char))
        for decimal in decimal_list:
            hexadecimal_list.append(decimal_to_hexadecimal(decimal))
        return ' '.join(str(hexadecimal) for hexadecimal in hexadecimal_list)
    else:
        return "[ERROR] -- Invalid string value"