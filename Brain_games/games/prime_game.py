from random import randint
from Brain_games.games.game_module import run_game
import math


def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i <= math.sqrt(number):
        if number % i < 1:
            return False
        i += 1
    return True


def generate_question_and_answer():
    random_number = randint(1, 50)
    question = f'Question: {random_number}'
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def game_of_prime():
    description = 'Answer "yes" if given number is prime. '\
                  'Otherwise answer "no".'
    run_game(description, generate_question_and_answer)
