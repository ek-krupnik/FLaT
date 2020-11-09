from constants import *


def ReversingMachineEdges(machine):

    reversed_machine = {}
    for from_state in machine.keys():
        for to_state in machine[from_state].keys():
            try:
                reversed_machine[to_state][from_state] = machine[from_state][to_state]
            except Exception:
                reversed_machine[to_state] = {from_state : machine[from_state][to_state]}

    return reversed_machine


# machine - dict from_state : {to_state : [letter,], }
def FindShortestWordLen(machine, x, k):
    # solve problem to prefix with reversed machine
    reversed_machine = ReversingMachineEdges(machine)
    # BFS
    # end state in reversed_machine is start in original
    # first -> state, second -> cnt of steps to this state
    stack = [(1, 0)]
    possible_answer = [INF]
    while len(stack) > 0:

        # print(stack)
        pair = stack.pop()
        current_state = pair[0]
        current_step = pair[1]

        for to in reversed_machine[current_state].keys():
            # print(reversed_machine[current_state].keys())
            for letter in reversed_machine[current_state][to]:

                # print(reversed_machine[current_state][to])
                # print(k, current_step, current_state, to, letter)

                if letter == '1' and current_step < min(possible_answer):
                    stack.append((to, current_step))
                    # print('here')
                    continue

                if k > current_step and letter == x and current_step + 1 < min(possible_answer):
                    stack.append((to, current_step + 1))
                    # print(stack)
                    continue
                if k <= current_step:
                    # terminate state
                    if to == 0:
                        # print('find', current_step, current_state)
                        possible_answer.append(current_step + 1)
                    elif current_step + 1 < min(possible_answer):
                        stack.append((to, current_step + 1))

    if min(possible_answer) == INF:
        return 'INF'
    else:
        return str(min(possible_answer))