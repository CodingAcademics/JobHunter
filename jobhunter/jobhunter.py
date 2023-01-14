from game_logic import GameLogic
import textwrap
import pyfiglet


def play():
    accepted = invite()


def invite():
    print(pyfiglet.figlet_format("Welcome to\nJob Hunter", font="slant", justify="center"))
    # width = 200 style="light_steel_blue"
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice == "y"


def decline_game():
    print("OK. Maybe another time")


if __name__ == '__main__':
    play()
