import random


def roll_the_dice(name="player"):
    while True:
        roll_one = random.randint(1, 6)
        roll_two = random.randint(1, 6)
        player_one = roll_one + roll_two

        print(f"{name} rolls the dice!")
        print(f"it's a {roll_one} and {roll_two}!")

        roll_one = random.randint(1, 6)
        roll_two = random.randint(1, 6)
        player_two = roll_one + roll_two

        print(f"computer rolls the dice!")
        print(f"it's a {roll_one} and {roll_two}!")

        if player_one > player_two:
            print(f'{name} wins!')
        elif player_one < player_two:
            print('computer wins!')
        else:
            print("it's a tie!")

        while True:
            do_continue = input(
                f"would you like to play again {name}? yes or no?\n").lower().strip()
            if do_continue == 'yes':
                break
            elif do_continue == "no":
                print(f"come back soon {name}!")
                return
            else:
                print("it's a yes or no question!")
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
    roll_the_dice(args.name)
