from random import choice, randint
import prompt


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression')
    tries = 0
    operations = ['*', '+', '-']
    while tries < 3:
        operation = choice(operations)
        random_number1 = randint(1, 25)
        random_number2 = randint(1, 25)
        print(f'Question: {random_number1} {operation} {random_number2}')
        answer = prompt.string('Your answer: ')
        correct_answer = eval(
            f'{random_number1} {operation} {random_number2}'
        )
        if answer == str(correct_answer):
            print('Correct!')
            tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            return print(f"Let's try again, {name}!")
    if tries == 3:
        print(f'Congratulations, {name}!')
