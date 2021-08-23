import sys
import random

def getLenPIN():
    len = int(input("Input length PIN: "))
    return len

def generatePIN():
    pin = ""
    for i in range(getLenPIN()):
        temp = random.SystemRandom().randint(0,9)
        pin += str(temp)
    print("PIN : ")
    return pin;

print(generatePIN());
