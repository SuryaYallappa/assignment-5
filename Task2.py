from calendar import error
from math import log, sin, sqrt

def sqt(digit):
    if digit<=0:
        print("Please enter a positive number")
    else:
        print(f"Square root : {sqrt(digit)}")

def logarithm(digit):
    if digit<=0:
        print("Please enter a positive number")
    else:
        print(f"Logarithm :{log(digit)}")

def sinex(digit):
    print(f"Sine :{sin(digit)}\n")

while True:
    try:
        num = float(input("Enter A Number: "))

        sqt(num)
        logarithm(num)
        sinex(num)
        break

    except ValueError:
        print("Please Enter A Valid Number")