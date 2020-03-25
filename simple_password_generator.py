import string
import random


def Generate_Password(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 9)  # only random numbers
        x = random.randint(10, 34)  # lower case chars
        x = random.randint(0, 94)
        password += string.printable[x]
    return password


print(Generate_Password(16))
