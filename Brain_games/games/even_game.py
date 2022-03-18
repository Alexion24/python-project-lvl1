from random import randint
from Brain_games.game_module import run_game


MIN_NUM = 1
MAX_NUM = 100


def generate_question_and_answer():
    random_number = randint(MIN_NUM, MAX_NUM)
    question = f'{random_number}'
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def game_of_even():
    description = 'Answer "yes" if the number is even, ' \
                  'otherwise answer is "no".'
    run_game(description, generate_question_and_answer)
