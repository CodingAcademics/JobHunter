import pyfiglet
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
import time

import indeed
import simplyhired
import zip_recruiter


def search_job(scraper_func, skill, city, pages):
    for _ in track(range(100), description='Searching Jobs....'):
        time.sleep(0.05)
    scraper_func(skill, city, pages)


def welcome():
    print(pyfiglet.figlet_format("Welcome to\nJob Hunter", font="slant", justify="center"))
    print("Would you like us to search for a job (y)es or (n)o?")
    choice = input("> ").lower()
    if choice == "y":
        your_job()
    if choice == "n":
        print("OK. Maybe another time")


def your_job():
    skill = input('What position are you searching for: ').strip()
    city = input('Enter the location: ').strip()
    pages = int(input('How many pages do you want us to search through: '))

    MARKDOWN = """
                                         OVERVIEW
    1. Indeed
    2. SimplyHired
    3. Zip Recruiter
    """

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

    choice = int(input("> "))

    if choice == 1:
        search_job(indeed.scraper_indeed, skill, city, pages)
    elif choice == 2:
        search_job(simplyhired.scraper_simply_hired, skill, city, pages)
    elif choice == 3:
        search_job(zip_recruiter.scraper_zip_recruiter, skill, city, pages)


if __name__ == '__main__':
    welcome()
