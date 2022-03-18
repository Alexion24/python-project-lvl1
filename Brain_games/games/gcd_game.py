from random import randint
from Brain_games.game_module import run_game
import math


MIN_NUM = 1
MAX_NUM = 25


def generate_question_and_answer():
    random_number1 = randint(MIN_NUM, MAX_NUM)
    random_number2 = randint(MIN_NUM, MAX_NUM)
    question = f'{random_number1} {random_number2}'
    correct_answer = math.gcd(random_number1, random_number2)
    return question, correct_answer


def game_of_gcd():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(description, generate_question_and_answer)
