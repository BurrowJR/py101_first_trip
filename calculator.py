''' This is a calculator.'''

def prompt(message):
    print(f'===> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to Calculator!")
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What is the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt("You must enter 1, 2, 3, 4")
    operation = input()

match operation:
    case '1':  # represents addition
        output = int(number1) + int(number2)
    case'2': #represents subtraction
        output = int(number1) - int(number2)
    case '3': #represents multiplication
        output = int(number1) * int(number2)
    case '4': #represents division
        output = int(number1) / int(number2)

print(f'The result is: {output}.')
