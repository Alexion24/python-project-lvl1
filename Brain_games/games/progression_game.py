import prompt
from random import randint, choice


def progression():
    prog_start = randint(1, 10)
    prog_step = randint(1, 10)
    prog_range = randint(5, 10)
    prog_list = [prog_start]
    prog_char = prog_start
    for i in range(prog_range):
        prog_char += prog_step
        prog_list.append(prog_char)
    hidden_char = choice(prog_list)
    question_prog = []
    for num in prog_list:
        if hidden_char == num:
            question_prog.append('..')
        else:
            question_prog.append(str(num))
    question_prog = ' '.join(question_prog)
    print('Question: {}'.format(question_prog))

    return hidden_char


def run_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    tries = 0
    while tries < 3:
        hidden_char = progression()
        answer = prompt.string('Your answer: ')
        if answer == str(hidden_char):
            print('Correct!')
            tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{hidden_char}'")
            return print(f"Let's try again, {name}!")
    if tries == 3:
        print(f'Congratulations, {name}!')
