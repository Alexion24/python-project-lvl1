import prompt


ROUND_COUNT = 3


def check_answer(answer, correct_answer):
    if answer == str(correct_answer):
        print('Correct!')
        return True
    else:
        print(
            "'{}' is wrong answer ;(. "
            "Correct answer was '{}'.".format(answer, correct_answer)
        )
        return False


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(description, game_data):
    name = welcome_user()
    print(description)
    for _ in range(ROUND_COUNT):
        question, correct_answer = game_data()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if not check_answer(answer, correct_answer):
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
