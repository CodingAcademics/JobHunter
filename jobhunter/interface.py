import pyfiglet
from prettytable import PrettyTable
# start will take the input of the user and move it into the scraping paramaters
# def start():
#   pass


def welcome():
    print(pyfiglet.figlet_format(
        "Welcome to\nJob Hunter", font="slant", justify="center"))
    print(
        """
    *******************************************************
    *** would you like us to find possible jobs for you ***
    *******************************************************
    """)
    print("(y)es I would like to look for a job or (n)o to exit")
    choice = input("> ")
    if choice == "y":
        your_job()
    if choice == "n":
        print("OK. Maybe another time")


def your_job():
    print(
        """
    *******************************************************
    ***** What type of position are you looking for? ******
    ******************************************************* 
    """)
    job = input("> ").lower()
    print(job)
    print("Would you like to filter by e(x)perience, (S)alary , or if (R)emote ")
    filter = input("> ").lower()
    if filter == "x":
        filtered_string = "experience"
    elif filter == "s":
        filtered_string = "salary"
    elif filter == "r":
        filtered_string = "if remote"

    print(
        f"""                   
                            /\/\/\/\/
                            |  0 0  |
                            | \___/ |
_______________________ooo__\_______/______________________________________
                                                                          
*** Now searching for positons like {job} filtered by {filtered_string} ***      
______________________________________ooo__________________________________
                             |  |  |
                             |_ | _|
                             |  |  |
                             |__|__|
                            (__/ \__)
  """)



    table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])

    tab.add_column('col 5', [-123, 43], align='r', valign='t')
    print(tab)
    


# def play_round(round_number, roller=GameLogic.roll_dice):
#     # unbanked_points = 0
#     dice_not_kept = 6
#     # kept_score = []
#     round_score = 0
#     print(f"Starting round {round_number}")
#     while True:
#         roll_string = ""
#         roll = roller(dice_not_kept)
#         #roll = (1, 1, 1, 1, 1, 1)
#         for x in roll:
#             roll_string += str(x) + " "
#         print(f"Rolling {dice_not_kept} dice...")
#         print(f"*** {roll_string} ***")
#         if GameLogic.calculate_score(roll) == 0:
#             print("****************************************")
#             print("**        Zilch!!! Round over         **")
#             print("****************************************")
#             round_score = 0
#             return round_score

#         # handles cheating uses validation function from GameLogic class

#         keepers = confirm_keepers(roll, roll_string)
#         if keepers == -1:
#             return -1
#         dice_not_kept -= len(keepers)
#         if dice_not_kept == 0:  # hot dice
#             dice_not_kept = 6  # reset to six
#         round_score += GameLogic.calculate_score(tuple(keepers))

#         print(f"You have {round_score} unbanked points and {dice_not_kept} dice remaining")
#         print("(r)oll again, (b)ank your points or (q)uit:")
#         choice_to_reroll = input("> ")
#         if choice_to_reroll == "b":
#             return round_score
#         if choice_to_reroll == "q":
#             return -1
#         #handle quitting by returning 0 / -1

#         # have the bank option in here somewhere


# def confirm_keepers(roll, roll_string):

#     while True:
#         #values = [int(value) for value in keeper_string if value.isdigit()]

#         #old solution
#         # for x in keepers:
#         #     all_kept_dice.append(int(x))
#         #     kept_score.append(int(x))

#         print("Enter dice to keep, or (q)uit:")
#         user_input_dice_to_keep = input("> ")

#         if user_input_dice_to_keep == "q":
#             return -1

#         formatted_user_input_dice_to_keep = [int(value) for value in user_input_dice_to_keep if value.isdigit()]

#         if GameLogic.validate_keepers(roll, formatted_user_input_dice_to_keep):
#             return formatted_user_input_dice_to_keep
#         else:
#             print("Cheater!!! Or possibly made a typo...")
#             print(f"*** {roll_string} ***")


# if __name__ == '__main__':
#     rolls = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
#     def mock_roller(rolls):
#         return (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)
#         #return rolls
welcome()
