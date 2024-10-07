negative = False
binary_negative = False
binary_twos_complement = False
twos_complement = False

def binary_conversion(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        if digit not in (0, 1):
            print("You have entered an invalid binary number")
            return
        decimal += digit * (2 ** power)
        power -= 1
    
    return decimal

def twos_complement_conversion(binary):
    n = len(binary)
    # Invert the bits
    for i in range(n):
        binary[i] = 1 - binary[i]
    # Add 1 to the inverted bits
    carry = 1
    for i in range(n-1, -1, -1):
        if binary[i] == 1 and carry == 1:
            binary[i] = 0
        else:
            binary[i] += carry
            carry = 0
    # Convert to decimal
    decimal = -binary_conversion(binary)
    return decimal

def sign_and_magnitude_conversion(binary):
    sign = -1 if binary[0] == 1 else 1
    binary[0] = 0  # Ignore the sign bit for magnitude
    decimal = binary_conversion(binary)
    return sign * decimal

def binary_to_decimal():
    global binary_negative
    global binary_twos_complement

    binary_input = input("Enter a binary number you want to convert to a decimal: ")
    if '.' in binary_input:
        print("Sorry you have entered a binary number with a decimal point")
        menu()
        return
    
    binary = list(map(int, binary_input))

    if binary[0] == 1:
        conversion_type = input("What type of conversion do you want to use?\n1) standard(non-negative)\n2) two's complement(negative)\n3) sign and magnitude\n")

        if conversion_type == "1":
            binary_negative = False
            decimal = binary_conversion(binary)
        elif conversion_type == "2":
            binary_twos_complement = True
            decimal = twos_complement_conversion(binary)
        elif conversion_type == "3":
            decimal = sign_and_magnitude_conversion(binary)
        else:
            print("Invalid conversion type selected.")
            return
    else:
        decimal = binary_conversion(binary)
    
    print(f"The decimal value is: {decimal}")
    menu()

def decimal_to_binary():
    global negative
    global twos_complement

    decimal = int(input("Enter a decimal number you want to convert to binary: "))

    if decimal < 0:
        conversion_type = int(input("Would You Like to Convert This Number Using:\n1) Sign and Magnitude\n2) Two's Complement\n"))

    if conversion_type > 2 or conversion_type < 1:
      print("Invalid Choice - 1 for Sign and Magnitude and 2 for Two's Complement\n")
      decimal_to_binary()
      return

    if conversion_type == 1:
        negative = True
        twos_complement = False
        decimal = -decimal
        binary_number = decimal_conversion(decimal)
        print(f"\n{decimal} Converted Using Sign and Magnitude to a Binary Number is {binary_number}\n")
    elif conversion_type == 2:
        negative = False
        twos_complement = True
        decimal = -decimal
        binary_number = decimal_conversion(decimal)
        decimal = -decimal
        print(f"\n{decimal} Converted Using Two's Complement to a Binary Number is {binary_number}\n")

    else:
        negative = False
        twos_complement = False
        binary_number = decimal_conversion(decimal)
        print(f"\n{decimal} Converted Using Standard Binary Conversion is {binary_number}\n")
    menu()

def decimal_conversion(decimal):
    binary = []

    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal // 2

    if negative:
        binary.append(1)

    if twos_complement:
        while len(binary) %2 != 0:
            binary.append(0)

    for i in range(len(binary)):
        binary[i] = 1 - binary[i]

    carry = 1
    for i in range(len(binary)):
      binary[i] += carry
      if binary[i] > 1:
        binary[i] = 0
        carry = 1
      else:
        carry = 0

    binary_number = "".join(map(str, binary[::-1]))
    return binary_number

def menu():
    user_input = str(input("Choose 1, 2 or 3:\n1) convert binary to decimal\n2) convert decimal to binary\n3) exit program\n"))
    if user_input == "1":
        binary_to_decimal()
    elif user_input == "2":
        decimal_to_binary()
    elif user_input == "3":
        exit()
    else:
        print("You have not selected 1, 2 or 3. Choose again:")
        menu()

menu()
