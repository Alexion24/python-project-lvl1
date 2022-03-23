from random import choice, randint
from Brain_games.game_module import run_game


MIN_NUM = 1
MAX_NUM = 25


def generate_question_and_answer():
    operations = ['*', '+', '-']
    operation = choice(operations)
    random_number1 = randint(MIN_NUM, MAX_NUM)
    random_number2 = randint(MIN_NUM, MAX_NUM)
    question = f'{random_number1} {operation} {random_number2}'
    correct_answer = False
    if operation == '*':
        correct_answer = random_number1 * random_number2
    elif operation == '+':
        correct_answer = random_number1 + random_number2
    elif operation == '-':
        correct_answer = random_number1 - random_number2
    return question, correct_answer


def game_of_calc():
    description = 'What is the result of the expression?'
    run_game(description, generate_question_and_answer)
