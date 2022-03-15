from random import choice, randint
from Brain_games.games.game_module import run_game


def generate_question_and_answer():
    operations = ['*', '+', '-']
    operation = choice(operations)
    random_number1 = randint(1, 25)
    random_number2 = randint(1, 25)
    question = f'Question: {random_number1} {operation} {random_number2}'
    correct_answer = eval(
        f'{random_number1} {operation} {random_number2}'
    )
    return question, correct_answer


def game_of_calc():
    description = 'What is the result of the expression?'
    run_game(description, generate_question_and_answer)
