from constants import *


def ParseRegExp(input_string):
    stack = []
    # creating regular expression
    for symbol in input_string:
        if symbol in LETTERS:
            stack.append(symbol)
        elif symbol in OPERATIONS:

            if len(stack) < 1:
                ReturnError(CurrentStackErrorMessage)
            first_element = stack.pop()

            new_element = ''
            if symbol == '*':
                new_element = '(' + first_element + ')*'
            else:

                if len(stack) < 1:
                    ReturnError(CurrentStackErrorMessage)
                second_element = stack.pop()

                if symbol == '.':
                    new_element = second_element + first_element
                elif symbol == '+':
                    new_element = '(' + second_element + symbol + first_element + ')'

            stack.append(new_element)

        else:
            ReturnError(InputValueErrorMessage)

    if len(stack) != 1:
        ReturnError(ResultStackErrorMessage)

    return stack[0]
