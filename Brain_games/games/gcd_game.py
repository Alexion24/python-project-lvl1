from random import randint
import prompt
import math


def game_of_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    tries = 0
    while tries < 3:
        random_number1 = randint(1, 25)
        random_number2 = randint(1, 25)
        print(f'Question: {random_number1} {random_number2}')
        answer = prompt.string('Your answer: ')
        gcd = math.gcd(random_number1, random_number2)
        if answer == str(gcd):
            print('Correct!')
            tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{gcd}'")
            return print(f"Let's try again, {name}!")
    if tries == 3:
        print(f'Congratulations, {name}!')
