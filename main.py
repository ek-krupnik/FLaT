from create_machine import *
from create_regexp import *
from passing_machine import *


def main(input_string):
    if len(input_string) < NumberOfArguments:
        ReturnError(InputArgumentSizeError)

    reg_exp = ParseRegExp(input_string[0])

    # dict from_state : {to_state : [letter,], }
    machine = CreateFiniteStateMachine(reg_exp)

    x = input_string[1]
    k = -1
    try:
        k = int(input_string[2])
    except TypeError:
        ReturnError(InputArgumentTypeError)

    answer = FindShortestWordLen(machine, x, k)
    return answer


if __name__ == "__main__":
    input_string = input().split(' ')
    print(main(input_string))
