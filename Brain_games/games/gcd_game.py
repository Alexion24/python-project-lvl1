from random import randint
from Brain_games.games.game_module import run_game
import math


def generate_question_and_answer():
    random_number1 = randint(1, 25)
    random_number2 = randint(1, 25)
    question = f'Question: {random_number1} {random_number2}'
    correct_answer = math.gcd(random_number1, random_number2)
    return question, correct_answer


def game_of_gcd():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(description, generate_question_and_answer)
