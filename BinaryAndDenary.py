def binarytodecimal():

    binary = input("Enter a binary number you want to convert to a decimal: ")
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        if digit not in ('0', '1'):
            print("You have entered an invalid binary number")
            return
        decimal += int(digit) * (2 ** power)
        power -= 1
    
    print(f"The decimal value of {binary} is: {decimal}")

def decimaltobinary():

    decimal = int(input("Enter a decimal number that you want to convert to binary: "))
    if decimal < 0:
        print("Sorry, you havr entered a negative number")
        return
    else:
        original_decimal = decimal
        binary_str = ""

        if decimal == 0:
            binary_str = "0"
        else:
            while decimal > 0:
                binary_str = str(decimal % 2) + binary_str
                decimal = decimal // 2
        
        print(f"The binary value of {original_decimal} is: {binary_str}")

def menu():
    user_input = str(input("Choose 1, 2 or 3:\n1) convert binary to decimal\n2) convert decimal to binary\n3) exit program\n"))
    if user_input == "1":
        binarytodecimal()
    elif user_input == "2":
        decimaltobinary()
    elif user_input == "3":
        exit()
    else:
        print("You have not selected 1, 2 or 3. Choose again:")
        menu()

menu()