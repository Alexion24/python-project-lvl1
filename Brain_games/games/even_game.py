from random import randint
from Brain_games.games.game_module import run_game


def generate_question_and_answer():
    random_number = randint(1, 100)
    question = f'Question: {random_number}'
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def game_of_even():
    description = 'Answer "yes" if the number is even, ' \
                  'otherwise answer is "no".'
    run_game(description, generate_question_and_answer)
