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

welcome()
