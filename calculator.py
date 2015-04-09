"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here



x = True

while x == True:

    input = raw_input("Enter an operator, and numbers: ")

    tokens = input.split(" ")  
    tokens_len = len(tokens)

    operator = tokens[0] 

    if tokens_len >= 2:
        num1 = float(tokens[1])

    if tokens_len == 3:
        num2 = float(tokens[2])

    if operator == "quit":  
        x = False
        print "Ok, bai!"

    def calculator():               
        
        if operator == "pow":
            print power(num1,num2)

        elif operator == "+":
            print add(num1, num2)

        elif operator == "-":
            print subtract(num1, num2)

        elif operator == "*":
            print multiply(num1, num2)

        elif operator == "/":
            print divide(num1, num2)

        elif operator == "square":
            print square(num1)

        elif operator == "cube":
            print cube(num1)

        elif operator == "mod":
            print mod(num1, num2)

    calculator()