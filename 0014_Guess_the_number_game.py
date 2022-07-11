import random
import os


clear = lambda: os.system('cls')
target_number = random.randint(1, 100)
chances_remaining = 0
player_guesses = []
tip_helper = {'low': 'Unknown', 'high': 'Unknown'}



def guess_checker(player_guess):
    clear()
    if player_guess > target_number:
        try:
            if tip_helper['high'] > player_guess:
                tip_helper['high'] = player_guess
        except TypeError:
            tip_helper['high'] = player_guess
        print('Too high. ')
        print(f"Your guesses: {''.join(str(player_guesses))}. "
              f"Number is between {tip_helper['low']} and {tip_helper['high']}")
    elif player_guess < target_number:
        try:
            if tip_helper['low'] < player_guess:
                tip_helper['low'] = player_guess
        except TypeError:
            tip_helper['low'] = player_guess
        print('Too low. ')
        print(f"Your guesses: {''.join(str(player_guesses))}. "
              f"Number is between {tip_helper['low']} and {tip_helper['high']}")
    elif player_guess == target_number:
        print(f"Your guesses: {''.join(str(player_guesses))}. ")
        print(f'You win! The number was {target_number}')
        quit()
    ask_for_guesses()


def ask_for_guesses():
    global chances_remaining
    if chances_remaining == 0:
        print(f'You lose! Sorry the number was {target_number}')
    else:
        print(f'You have {chances_remaining} attempts remaning to guess the number. ')
        player_guess = int(input('Make a guess. '))
        player_guesses.append(player_guess)
        chances_remaining -= 1
        guess_checker(player_guess)


print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
diff_choice = input('Choose a difficulty. Type "easy" or "hard": ')

if diff_choice.lower() == 'easy':
    chances_remaining = 10
elif diff_choice.lower() == 'hard':
    chances_remaining = 5

ask_for_guesses()
