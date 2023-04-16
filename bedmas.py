import random

def generate_expression(difficulty, operator):
    num1 = random.randint(1, 10 * difficulty)
    num2 = random.randint(1, 10 * difficulty)
    expression = f'{num1} {operator} {num2}'
    return expression

def generate_question(difficulty, operator):
    expression = generate_expression(difficulty, operator)
    question = f'What is the result of {expression}?'
    return question

def show_work(expression):
    num1, operator, num2 = expression.split()
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        result = num1 + num2
        work = f'{num1} + {num2} = {result}'
    elif operator == '-':
        result = num1 - num2
        work = f'{num1} - {num2} = {result}'
    elif operator == '*':
        result = num1 * num2
        work = f'{num1} * {num2} = {result}'
    elif operator == '/':
        result = num1 / num2
        work = f'{num1} / {num2} = {result}'
    return work

def check_answer(expression, answer):
    correct_answer = eval(expression)
    if answer == correct_answer:
        print('Correct!')
    else:
        print('Incorrect. Here\'s a hint:')
        print(show_work(expression))

print('Welcome to our math lesson! Today we will learn about basic math operations.')
print('There are four basic math operations: addition (+), subtraction (-), multiplication (*), and division (/).')
print('We will follow the BEDMAS order: Brackets, Exponents, Division, Multiplication, Addition, Subtraction.')
print('Let\'s start with addition!')

operators = ['+', '-', '*', '/']
for operator in operators:
    print(f'Now we will practice {operator}!')
    for i in range(5):
        expression = generate_expression(1, operator)
        question = generate_question(1, operator)
        work = show_work(expression)
        print(f'Example: {work}')
        print(f'Now it\'s your turn! {question}')
        answer = input('Enter your answer: ')
        check_answer(expression, int(answer))