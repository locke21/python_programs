def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2

operation_list = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

num1 = int(input('What is the first number? '))

while True:
    operation = input('Pick an Operation: + - / * ')
    num2 = int(input('What is the second number? '))
    answer = operation_list[operation](num1, num2)

    print(f'{num1} {operation} {num2} = {answer}')

    continue_question = input(f'Would you like to continue with {answer}? '
                              f'Type "y" to calculate with same number, '
                              f'"n" to start new calculaton, anything else to quit. ')
    if continue_question.lower() == "y":
        num1 = int(answer)
    elif continue_question.lower() == "n":
        num1 = int(input('What is the first number? '))
    else:
        quit()
