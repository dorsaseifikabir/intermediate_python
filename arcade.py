from rps_game import rock_paper_scissors
from dice_game import roll_the_dice
import number_guessing_game
import sys


def menu(name="player"):
    print(f"hello {name}! welcome to the arcade!\n")
    while True:
        print(f'''
            1. rock, paper scissors
            2. dice roll
            3. guess the number
            4. quit
            ''')
        play = input("which game do you want to play today?\n")
        if play == "1":
            rock_paper_scissors(name)
        elif play == "2":
            roll_the_dice(name)
        elif play == "3":
            max_guess = number_guessing_game.mode(name)
            number_guessing_game.guessing_game(name, max_guess)
        elif play == "4":
            sys.exit("come play again soon!")
        else:
            print(f"{name} you must choose from the menu!")
            continue


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="personalizing the game experience!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", default="player",
        help="enter player name."
    )

    args = parser.parse_args()
    menu(args.name)
