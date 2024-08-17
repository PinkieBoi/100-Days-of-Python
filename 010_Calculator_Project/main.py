import os
import art
from time import sleep


def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid Operand")
        sleep(3)
        exit()


def continue_calc(n):
    contd = input(f"Continue with {n} [y/N] or enter 'c' to exit:\t")
    if contd.lower() == "y":
        return True
    elif contd.lower() == "c":
        exit()
    else:
        return False


def calculator_app():
    os.system("clear")
    print(art.calculator)
    num1 = float(input("First Number:\t"))
    method = input("Select Operation (+ - * /)\n")
    num2 = float(input("Second Number:\t"))
    num3 = calculate(method, num1, num2)
    print(f"Answer:\n{num3}")
    while continue_calc(num3):
        os.system("clear")
        print(f"{art.calculator}\n\n{num3}")
        method = input("Select Operation (+ - * /)\n")
        num4 = float(input("Second Number:\t"))
        num3 = calculate(method, num3, num4)
        print(f"Answer:\n{num3}")
    calculator_app()


calculator_app()

