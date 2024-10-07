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
    is_negative = binary[0] == 1

    if is_negative:
        # Invert the bits
        binary = [1 - bit for bit in binary]
        # Add 1 to the inverted bits
        carry = 1
        for i in range(n-1, -1, -1):
            if binary[i] == 1 and carry == 1:
                binary[i] = 0
            else:
                binary[i] += carry
                carry = 0

    # Convert to decimal
    decimal = sum(bit * (2 ** i) for i, bit in enumerate(reversed(binary)))
    return -decimal if is_negative else decimal

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

    if decimal != "":
        decimal = int(decimal)
        conversion_type = int(input("Would You Like to Convert This Number Using:\n1) Sign and Magnitude\n2) Two's Complement\n3) Standard (non-negative)\n"))

        if conversion_type == 1:
            negative = True
            twos_complement = False
        elif conversion_type == 2:
            negative = False
            twos_complement = True
        elif conversion_type == 3:
            negative = False
            twos_complement = False
        else:
            print("Invalid conversion type selected.")
            return

        binary_str = decimal_conversion(decimal)
        print(f"The binary value is: {binary_str}")
    else:
        print("You have not entered a number")
        decimal_to_binary()


def decimal_conversion(decimal):
    global binary_str
    global negative
    global twos_complement

    binary_str = ""
    binary = []

    if decimal == 0:
        return "0"

    if decimal > 0:
        while decimal > 0:
            binary.append(decimal % 2)
            decimal = decimal // 2
        binary.reverse()
        binary_str = ''.join(map(str, binary))
        return binary_str

    elif decimal < 0:
        decimal = abs(decimal)
        while decimal > 0:
            binary.append(decimal % 2)
            decimal = decimal // 2
        binary.reverse()

        if negative:
            binary.insert(0, 1)

        if twos_complement:
            while len(binary) %8 != 0:
                binary.insert(0, 0)

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

       
        binary_str = ''.join(map(str, binary))
        return binary_str
        

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