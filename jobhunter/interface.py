import pyfiglet
from rich.console import Console
from rich.markdown import Markdown
from indeed import scraper_indeed
from simplyhired import scraper_simply_hired
from zip_recruiter import scraper_zip_recruiter


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
    # Skills & Place of Work
    skill = input('Enter your Skill: ').strip()
    city = input('Enter the location: ').strip()
    pages = int(input('Enter the # of pages you want to search: '))

    MARKDOWN = """
                                             OVERVIEW
    1. Indeed
    2. SimplyHired
    3. Zip Recruiter
    
    """

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

    choice = input("> ")

    if choice == "1":
        scraper_indeed(skill, city, pages)
    if choice == "2":
        scraper_simply_hired(skill, city, pages)
    if choice == "3":
        scraper_zip_recruiter(skill, city, pages)


if __name__ == '__main__':
    welcome()

# --------------------------------------------------------------------------------------------------

#     print(
#         """
#     *******************************************************
#     ***** What type of position are you looking for? ******
#     *******************************************************
#     """)
#     job = input("> ").lower()
#     print(job)
#     print("Would you like to filter by e(x)perience, (S)alary , or if (R)emote ")
#     filter = input("> ").lower()
#     if filter == "x":
#         filtered_string = "experience"
#     elif filter == "s":
#         filtered_string = "salary"
#     elif filter == "r":
#         filtered_string = "if remote"
#
#     print(
#         f"""
#                             /\/\/\/\/
#                             |  0 0  |
#                             | \___/ |
# _______________________ooo__\_______/______________________________________
#
# *** Now searching for positons like {job} filtered by {filtered_string} ***
# ______________________________________ooo__________________________________
#                              |  |  |
#                              |_ | _|
#                              |  |  |
#                              |__|__|
#                             (__/ \__)
#   """)
#
#
#
#     table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
#     tab = PrettyTable(table[0])
#     tab.add_rows(table[1:])
#
#     tab.add_column('col 5', [-123, 43], align='r', valign='t')
#     print(tab)
