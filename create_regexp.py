from constants import *


def ParseRegExp(input_string):
    stack = []
    # creating regular expression
    for symb in input_string:
        if symb in LETTERS:
            stack.append(symb)
        elif symb in OPERATIONS:

            if len(stack) < 1:
                ReturnError(CurrentStackError)
            first_element = stack.pop()

            new_element = ''
            if symb == '*':
                new_element = '(' + first_element + ')*'
            else:

                if len(stack) < 1:
                    ReturnError(CurrentStackError)
                second_element = stack.pop()

                if symb == '.':
                    new_element = second_element + first_element
                elif symb == '+':
                    new_element = '(' + second_element + symb + first_element + ')'

            stack.append(new_element)

        else:
            ReturnError(InputValueError)

    if len(stack) != 1:
        ReturnError(ResultStackError)

    return stack[0]
