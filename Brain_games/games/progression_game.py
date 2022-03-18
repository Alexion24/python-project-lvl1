from Brain_games.game_module import run_game
from random import randint, choice


MIN_START = 0
MAX_START = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_RANGE = 5
MAX_RANGE = 10


def generate_question_and_answer():
    prog_start = randint(MIN_START, MAX_START)
    prog_step = randint(MIN_STEP, MAX_STEP)
    prog_range = randint(MIN_RANGE, MAX_RANGE)
    prog_list = [prog_start]
    prog_char = prog_start
    for i in range(prog_range):
        prog_char += prog_step
        prog_list.append(prog_char)
    correct_answer = choice(prog_list)
    question_prog = []
    for num in prog_list:
        if correct_answer == num:
            question_prog.append('..')
        else:
            question_prog.append(str(num))
    question_prog = ' '.join(question_prog)
    question = '{}'.format(question_prog)
    return question, correct_answer


def game_of_progressions():
    description = 'What number is missing in the progression?'
    run_game(description, generate_question_and_answer)
