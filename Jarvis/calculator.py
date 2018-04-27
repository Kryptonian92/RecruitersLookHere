from arithmetic import addition, multiplication, division, subtraction
from checks import exitCheck, numCheck, symCheck

def math():
    num1 = input("Enter the first number ")
    while not numCheck(num1):
        print("Invalid input, please try again.")
        num1 = input("Enter the first number ")
    num1 = int(num1)
    num2 = input("Enter the second number ")
    while not numCheck(num2):
        print("Invalid input, please try again.")
        num2 = input("Enter the second number ")
    num2 = int(num2)
    symbol = input("What operation do you want to perform? (+,-,*,/) ")
    while not symCheck(symbol):
        print("Invalid input, please try again.")
        symbol = input("What operation do you want to perform? (+,-,*,/) ")

    if symbol == "+":
        print(num1, "+", num2, "=", addition(num1,num2))
    elif symbol == "-":
        print(num1, "-", num2, "=",subtraction(num1,num2))
    elif symbol == "*":
        print(num1, "*", num2, "=",multiplication(num1,num2))
    elif symbol == "/":
        print(num1, "/", num2, "=",division(num1,num2))
