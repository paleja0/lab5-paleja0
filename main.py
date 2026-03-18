import math
from utils_calc import *


while True:
    operacion = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()
    
    if operacion == "exit":
        break

    elif operacion == "add":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", add(num1, num2))

    elif operacion == "subtract":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", sub(num1, num2))

    elif operacion == "multiply":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", multiply(num1, num2))

    elif operacion == "divide":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", divide(num1, num2))

    elif operacion == "exponent":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", exponent(num1, num2))

    elif operacion == "modulo":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
       
        print("The result is:", modulo(num1, num2))

    elif operacion == "floor_divide":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", floor_divide(num1, num2))

    elif operacion == "absolute":
        num = float(input("Enter the number:\n"))
        print("The result is:", absolute(num))

    else:
        print("Invalid option!")