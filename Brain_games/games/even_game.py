from random import randint
import prompt


def game_of_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer is "no"')
    tries = 0
    while tries < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == 'yes' \
                or random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            tries += 1
        elif random_number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
            return print(f"Let's try again, {name}!")

        elif random_number % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return print(f"Let's try again, {name}!")
    if tries == 3:
        print(f'Congratulations, {name}!')
