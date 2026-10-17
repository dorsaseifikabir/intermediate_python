import random

rules = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}

rps_choices = {
    '1': ('r', 'rock'),
    '2': ('p', 'paper'),
    '3': ('s', 'scissors')
}

choices = {}

for num, (letter, rps) in rps_choices.items():
    choices[num] = rps
    choices[letter] = rps
    choices[rps] = rps


def rock_paper_scissors(name="player"):
    while True:
        player_wins = 0
        computer_wins = 0
        round_number = 1
        while round_number <= 3 or player_wins == computer_wins:
            while True:
                print('rps'.center(20, "="))
                for num, letter in rps_choices.items():
                    print(f"{num}. {rps_choices[num][1]}")
                player_choice = input(
                    f"which is it {name}, rock, paper or scissors? "
                ).lower().strip()

                if player_choice in choices:
                    player_choice = choices[player_choice]
                    break
                else:
                    print(f"{name} Please choose one of the given options.")
                    continue

            pc_choice = random.choice(list(rules))

            if round_number > 3:
                print(
                    f"\nohoh! lets continue untill we have a winner. good luck {name}!\n")
                print(f"round {round_number}:\n")
            else:
                print(f"\nround {round_number}:\n")

            if player_choice == pc_choice:
                print("It's a tie!")

            elif pc_choice == rules[player_choice]:
                print(f"congratz {name}, you win!🥳")
                player_wins += 1

            else:
                print(f"You lose, sorry {name}...😢")
                computer_wins += 1

            print(f"Computer chose: {pc_choice}")
            print(f"{name}'s total wins: {player_wins}")
            print(f"Computer total wins: {computer_wins}")
            print()

            round_number += 1

        if player_wins > computer_wins:
            print(f"{name} is the winner!🥳")
        else:
            print(f"The computer wins...sorry {name}...😢")

        while True:
            do_continue = input(
                f"would you like to play again {name}? yes or no?\n").lower().strip()
            if do_continue == 'yes':
                break
            elif do_continue == "no":
                print(f"see you soon {name}!")
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
    rock_paper_scissors(args.name)
