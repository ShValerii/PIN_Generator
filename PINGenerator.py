import sys
import random

def getLenPIN():
    len = int(input("Input length PIN: "))
    return len

def generatePIN():
    frontpin = ''
    endpin=''
    len = getLenPIN()
    for i in range(len//2):
        temp = random.SystemRandom().randint(0,9)
        endpin += str(temp)
    for j in range(len-(len//2)):
        temp1 = random.SystemRandom().randint(0, 9)
        frontpin = str(temp1) + str(frontpin)
    print("PIN : ")
    return str(frontpin)+ str(endpin);

print(generatePIN());
