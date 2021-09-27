from constants import *
from collections import namedtuple


def GetExpressionAnderOperation(expression):
    # returning namedtuple [operation, first_argument, second_argument = '']
    ParsedExpression = namedtuple('ParsedExpression', 'operation first_argument second_argument')

    if expression.count('(') != expression.count(')'):
        ReturnError(BracketBalanceError)

    # (result)*
    if expression[-1] == '*' and expression[0] == '(' and expression[-2] == ')':
        return ParsedExpression(operation='*', first_argument=expression[1:-2], second_argument='')

    # (first_argument + second_argument)
    # brackets balanced check

    # (a+b)
    if expression.count('(') != 0 and expression[1:-1].count('(') == 0 and expression[1:-1].count(')') == 0:
        plus_index = expression.find('+')
        return ParsedExpression(operation='+', first_argument=expression[1:plus_index],
                                second_argument=expression[plus_index + 1:-1])

    balance = 0
    plus_position = -1
    if expression[0] == '(' and expression[-1] == ')':
        for i, symbol in enumerate(expression[1:-1]):
            if symbol == '(':
                balance += 1
            if symbol == ')':
                balance -= 1
            if balance < 0:
                plus_position = -1
                break
            if balance == 0 and symbol == '+':
                if plus_position != -1:
                    ReturnError(PlusParsingError)
                plus_position = i + 1

    # (S) or S -> divide on S = KT
    if plus_position == -1:
        i = 0
        j = len(expression)

        balance = 0
        divide_index = -1
        for it, symbol in enumerate(expression):
            if symbol == '(':
                balance += 1
            if symbol == ')':
                balance -= 1
            # cut first independent part as K
            if balance == 0:
                divide_index = it + 1
                break
        if divide_index < len(expression) and expression[divide_index] == '*':
            divide_index += 1

        return ParsedExpression(operation='.', first_argument=expression[i: divide_index],
                                second_argument=expression[divide_index: j])

    return ParsedExpression(operation='+', first_argument=expression[1:plus_position],
                            second_argument=expression[plus_position + 1:-1])


def AddArgument(machine, from_state, to_state, argument):
    try:
        machine[from_state][to_state].append(argument)
    except Exception:
        machine[from_state][to_state] = [argument]


# get machine and namedtuple [operation, first_argument, second_argument = '']
def AddTransition(state_count, machine, from_state, to_state, transition):
    operation = transition.operation
    first_argument = transition.first_argument
    second_argument = transition.second_argument

    # from_state -(first_argument.second_argument)-> to_state
    # to
    # from_state -(first_argument)-> new_state -(second_argument)-> to_state
    if operation == '.':
        # add new state
        new_state = state_count
        state_count += 1
        machine[from_state][new_state] = [first_argument]
        machine[new_state] = {to_state: [second_argument]}

    # from_state -(first_argument + second_argument)-> to_state
    # to
    # from_state -(first_argument)-> to_state
    # from_state -(second_argument)-> to_state
    if operation == '+':
        machine[from_state][to_state].append(first_argument)
        machine[from_state][to_state].append(second_argument)

    # from_state -(first_argument)*-> to_state
    # to
    # from_state -(first_argument)-> from_state
    # from_state -(1)-> to_state
    if operation == '*':
        AddArgument(machine, from_state, from_state, first_argument)
        machine[from_state][to_state].append('1')

    return state_count, machine


def PassTransition(machine, from_state, to_state, state_count, end):

    start_end = end
    start_state_count = state_count
    start_machine = machine
    try:
        for transition in machine[from_state][to_state]:
            if len(transition) > 1:
                end = False
                # delete it from machine
                machine[from_state][to_state].remove(transition)
                # adding new
                state_count, machine = AddTransition(state_count, machine, from_state, to_state,
                                                     GetExpressionAnderOperation(transition))

    # there is no such transition
    except KeyError:
        return start_end, start_state_count, start_machine

    return end, state_count, machine


# dict from_state : {to_state : [letter,], }
# start state = 0
# end state in beginning =1
def CreateFiniteStateMachine(reg_exp):
    machine = {0: {1: [reg_exp]}}
    # terminate_state is 1 (and only it because of adding 1-transitions)
    state_count = 2
    end = False
    while not end:
        end = True
        out_states = state_count

        for from_state in range(out_states):
            for to_state in range(out_states):

                end, state_count, machine = PassTransition(machine, from_state, to_state, state_count, end)

    return machine
