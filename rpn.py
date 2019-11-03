#!/usr/bin/env python3

import operator
import readline
import colorama

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

RED = '\033[31m'
BLUE = '\u001b[44m'
MAGENTA = '\u001b[35m'
RESET = '\033[0m'

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            colored = BLUE + "Calculation: " + RESET + str(arg1) + MAGENTA + token + RESET + str(arg2) + " = "
            if (result < 0):
                colored += RED
            colored += str(result) + RESET
            stack.append(result)
            print(colored)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

# def random_func():
#     print("something")

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
