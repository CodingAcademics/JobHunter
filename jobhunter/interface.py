import pyfiglet
from rich.console import Console
from rich.markdown import Markdown
from indeed import scraper_indeed
from simplyhired import scraper_simply_hired
from zip_recruiter import scraper_zip_recruiter
from rich.progress import track
import time


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
        for i in track(range(100), description='Searching Jobs....'):
            time.sleep(0.02)
        scraper_indeed(skill, city, pages)
    if choice == "2":
        for i in track(range(100), description='Searching Jobs....'):
            time.sleep(0.20)
        scraper_simply_hired(skill, city, pages)
    if choice == "3":
        for i in track(range(100), description='Searching Jobs....'):
            time.sleep(0.20)
        scraper_zip_recruiter(skill, city, pages)


if __name__ == '__main__':
    welcome()
