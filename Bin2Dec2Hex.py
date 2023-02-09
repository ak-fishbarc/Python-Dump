# Binary to Decimal to Hexadecimal
def add_zeroes(bin_num):
    if len(bin_num) % 4 != 0:
        add_zero = 4 - (len(bin_num) % 4)
        to_add = "0" * add_zero
        bin_num = to_add + bin_num

    return bin_num


def check_input(bin_num):
    for letter in bin_num:
        if letter != "1" and letter != "0":
            print("Sorry, binary values must be only of 1 and 0.")
            break

    return bin_num


def bin2dec(bin_num):
    to_dec = 0
    i = 0
    while i < len(bin_num):
        if bin_num[(i+1)*(-1)] == "1":
            to_dec += 2 ** i
        i += 1

    return to_dec


def dec2hex(dec_num):
    hexadec = ""

    hex_letter = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    done = False
    while not done:
        remainder = (dec_num%16)
        value = int(dec_num/16)

        if remainder in hex_letter:
            hexadec += hex_letter[remainder]
        else:
            hexadec += str(remainder)

        if value == 0:
            done = True
        else:
            dec_num = value
    return hexadec[::-1]


user_input = input("Please specify binary value to conver:")

sanitized_input = check_input(user_input)
extended_num = add_zeroes(sanitized_input)
converted2dec = bin2dec(extended_num)
converted2hex = dec2hex(converted2dec)
print(converted2dec)
print(converted2hex)
