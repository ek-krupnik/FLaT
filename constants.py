def ReturnError(error_str):
    raise Exception(error_str)


INF = 1e9
NumberOfArguments = 3

ALPHABET = ['a', 'b', 'c', '1', '.', '+', '*']
LETTERS = ['a', 'b', 'c', '1']
OPERATIONS = ['.', '+', '*']

CommonErrorMessage = "ERROR : "
InputValueErrorMessage = "Wrong input value"
InputArgumentTypeErrorMessage = "Third argument should be integer"
InputArgumentSizeErrorMessage = "Wrong number of arguments"
ResultStackErrorMessage = "Wrong stack size after creating regexp"
CurrentStackErrorMessage = "Wrong stack size during parsing"

PlusParsingError = "There is more than one plus in one bracket"
BracketBalanceError = "Wrong bracket balance"
