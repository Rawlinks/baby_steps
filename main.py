# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import seed, choice, randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def what_would_beat(input):
    if input == 'rock':
        return 'paper'
    elif input == 'paper':
        return 'scissors'
    elif input == 'scissors':
        return 'rock'
    else:
        return f'what_would_beat: Invalid argument specified: {input}'


def make_a_selection():
    selection = choice(['rock', 'paper', 'scissors'])
    return selection


def decide_a_winner(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return 0
    elif player_1_choice == what_would_beat(player_2_choice):
        return 1
    else:
        return 2

def play_game():
    player_1_choice = make_a_selection()
    print(f'Player 1 chose {player_1_choice}')

    player_2_choice = make_a_selection()
    print(f'Player 2 chose {player_2_choice}')

    winner = decide_a_winner(player_1_choice, player_2_choice)

    if winner == 0:
        print('Its a Draw!')
    else:
        print(f'Player {winner} has won!')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

