import math

# Decimal, binary, octal & hexadecimal converter
# github.com/teodorandrei yeaaa


choice = input("Choose your converter: \n(1) Decimal to binary\n(2) Binary to decimal\n(3) Octal to decimal\n(4) Hexadecimal to decimal\n(5) Octal to binary\n(6) Hexadecimal to binary\n> Your choice: ")



def decimal_to_binary(x):
    y = ""
    while x>1: 
        if x % 2 == 0:
            y += "0"
        elif x % 2 == 1:
            y += "1"
        x = math.floor(x / 2)
    y += "1"
    y = y[::-1]
    return y

def binary_to_decimal(x):
    y = 0
    for i, cifra in enumerate(reversed(str(x))):
        y += int(cifra) * (2**i)

    return y

def octal_to_decimal(x):
    y = 0
    for i, cifra in enumerate(reversed(str(x))):
        y += int(cifra) * (8**i)

    return y

def hexadecimal_to_decimal(x):
    y = 0
    for i, cifra in enumerate(reversed(str(x))):
        match cifra.upper():
            case "A":
                y += 10 * (16**i)
            case "B":
                y += 11 * (16**i)
            case "C":
                y += 12 * (16**i)
            case "D":
                y += 13 * (16**i)
            case "E":
                y += 14 * (16**i)
            case "F":
                y += 15 * (16**i)
            case _:
                y += int(cifra) * (16**i)

    return y

def octal_to_binary(x):
   y = 0

   for i, cifra in enumerate(reversed(str(x))):
       y += int(cifra) * (8**i)
   z = ""
   while y > 1:
       if y%2==0:
           z += "0"
       elif y%2==1:
           z += "1"
       y = math.floor(y/2)
   z += "1"
   z = z[::-1]
   return z

def hexadecimal_to_binary(x):
    y = 0
    for i, cifra in enumerate(reversed(str(x))):
        match cifra.upper():
            case "A":
                y += 10 * (16**i)
            case "B":
                y += 11 * (16**i)
            case "C":
                y += 12 * (16**i)
            case "D":
                y += 13 * (16**i)
            case "E":
                y += 14 * (16**i)
            case "F":
                y += 15 * (16**i)
            case _:
                y += int(cifra) * (16**i)
    z = ""
    while y > 1:
        if y%2==0:
            z+="0"
        elif y%2==1:
            z+="1"
        y = math.floor(y/2)
    z += "1"
    z = z[::-1]
    return z

match choice.lower():
    case "1":
        number = input("Decimal to binary selected, please input your number: ")
        print(f"Input (base10): {str(number)} | Output (base2): {str(decimal_to_binary(int(number)))}")
    case "2":
        number = input("Binary to decimal selected, please input your number: ")
        print(f"Input (base2): {str(number)} | Output (base10): {str(binary_to_decimal(int(number)))}")
    case "3":
        number = input("Octal to decimal selected, please input your number: ")
        print(f"Input (base8): {str(number)} | Output (base10): {str(octal_to_decimal(int(number)))}")
    case "4":
        number = input("Hexadecimal to decimal selected, please input your number: ")
        print(f"Input (base16): {str(number)} | Output (base10): {str(hexadecimal_to_decimal(str(number)))}")
    case "5":
        number = input("Octal to binary selected, please input your number: ")
        print(f"Input (base8): {str(number)} | Output (base2): {str(octal_to_binary(int(number)))}")
    case "6":
        number = input("Hexadecimal to binary selected, please input your number: ")
        print(f"Input (base16): {str(number)} | Output (base2): {str(hexadecimal_to_binary(str(number)))}")

