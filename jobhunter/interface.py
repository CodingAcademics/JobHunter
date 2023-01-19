import pyfiglet
from rich.prompt import Prompt
from rich.progress import track
import time
from rich import print
from rich.panel import Panel

import indeed
import simplyhired
import zip_recruiter


def search_job(scraper_func, skill, city, pages):
    for _ in track(range(100), description='Searching Jobs....'):
        time.sleep(0.05)
    scraper_func(skill, city, pages)


def welcome():
    print(pyfiglet.figlet_format("Welcome to\nJob Hunter", font="slant", justify="center"))
    print(Panel.fit("[bold red]Would you like to search for a job?"))
    choice = Prompt.ask('> ',
                        choices=['y', 'n']).lower()
    if choice == "y":
        your_job()
    if choice == "n":
        print(Panel.fit("[bold red]OK. Maybe another time"))


def your_job():
    print(Panel.fit('[bold green]What position are you searching for? '))
    skill = Prompt.ask('> ').strip()
    print(Panel.fit('[bold blue]Enter the location: '))
    city = Prompt.ask('> ').strip()
    print(Panel.fit('[bold cyan]How many pages do you want us to search through? '))
    pages = int(Prompt.ask('> ').strip())

    print(pyfiglet.figlet_format("OVERVIEW", font="slant", justify="center"))
    print(Panel.fit("[bold blue]1. Indeed | [bold purple]2. SimplyHired | [bold green]3. Zip Recruiter", border_style='none', width=100))

    print(Panel.fit('[bold yellow]Which job board would you like to select?'))
    choice = int(Prompt.ask('> ',
                            choices=['1', '2', '3']))

    if choice == 1:
        search_job(indeed.scraper_indeed, skill, city, pages)
    elif choice == 2:
        search_job(simplyhired.scraper_simply_hired, skill, city, pages)
    elif choice == 3:
        search_job(zip_recruiter.scraper_zip_recruiter, skill, city, pages)


if __name__ == '__main__':
    welcome()
