from Brain_games.game_module import run_game
from random import randint, choice


def generate_question_and_answer():
    prog_start = randint(1, 10)
    prog_step = randint(1, 10)
    prog_range = randint(5, 10)
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
    question = 'Question: {}'.format(question_prog)

    return question, correct_answer


def game_of_progressions():
    description = 'What number is missing in the progression?'
    run_game(description, generate_question_and_answer)
