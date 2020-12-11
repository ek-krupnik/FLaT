from constants import *


# returning list [operation, first_argument, second_argument = '']
def GetExpressionAnderOperation(expression):
    if expression.count('(') != expression.count(')'):
        ReturnError(BracketBalanceError)

    # (result)*
    if expression[-1] == '*' and expression[0] == '(' and expression[-2] == ')':
        return ['*', expression[1:-2], '']

    # (first_argument + second_argument)
    # brackets balanced check

    # (a+b)
    if expression.count('(') != 0 and expression[1:-1].count('(') == 0 and expression[1:-1].count(')') == 0:
        plus_ind = expression.find('+')
        return ['+', expression[1:plus_ind], expression[plus_ind + 1:-1]]

    balance = 0
    plus_position = -1
    if expression[0] == '(' and expression[-1] == ')':
        for i, symb in enumerate(expression[1:-1]):
            if symb == '(':
                balance += 1
            if symb == ')':
                balance -= 1
            if balance < 0:
                plus_position = -1
                break
            if balance == 0 and symb == '+':
                if plus_position != -1:
                    ReturnError(PlusParsingError)
                plus_position = i + 1

    # (S) or S -> divide on S = KT
    if plus_position == -1:
        i = 0
        j = len(expression)

        balance = 0
        divide_ind = -1
        for it, symb in enumerate(expression):
            if symb == '(':
                balance += 1
            if symb == ')':
                balance -= 1
            # cut first independent part as K
            if balance == 0:
                divide_ind = it + 1
                break
        if divide_ind < len(expression) and expression[divide_ind] == '*':
            divide_ind += 1

        return ['.', expression[i: divide_ind], expression[divide_ind: j]]

    return ['+', expression[1:plus_position], expression[plus_position + 1:-1]]


def AddArgument(machine, from_state, to_state, argument):
    try:
        machine[from_state][to_state].append(argument)
    except Exception:
        machine[from_state][to_state] = [argument]


# get machine and list [operation, first_argument, second_argument = '']
def AddTransition(state_count, machine, from_state, to_state, transition):
    operation = transition[0]
    first_argument = transition[1]
    second_argument = transition[2]

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
                except Exception:
                    pass
    return machine
