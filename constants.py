def ReturnError(error_str):
    raise Exception(error_str)


INF = 1e9
NumberOfArguments = 3

ALPHABET = ['a', 'b', 'c', '1', '.', '+', '*']
LETTERS = ['a', 'b', 'c', '1']
OPERATIONS = ['.', '+', '*']

CommonErrorMessage = "ERROR : "
InputValueError = "Wrong input value"
InputArgumentTypeError = "Third argument should be integer"
InputArgumentSizeError = "Wrong number of arguments"
ResultStackError = "Wrong stack size after creating regexp"
CurrentStackError = "Wrong stack size during parsing"

PlusParsingError = "There is more than one plus in one bracket"
BracketBalanceError = "Wrong bracket balance"
