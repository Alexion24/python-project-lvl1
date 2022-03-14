from random import randint
import prompt
import math


def is_prime():
    random_number = randint(1, 50)
    print(f'Question: {random_number}')
    if random_number == 1:
        return 'no'
    i = 2
    while i <= math.sqrt(random_number):
        if random_number % i < 1:
            return 'no'
        i += 1
    return 'yes'


def game_of_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    tries = 0
    while tries < 3:
        correct_answer = is_prime()
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            tries += 1
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.".format(answer, correct_answer)
            )
            return print(f"Let's try again, {name}!")
    if tries == 3:
        print(f'Congratulations, {name}!')
