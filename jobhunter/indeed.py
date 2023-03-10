import cloudscraper
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.prompt import Prompt
import time
import warnings
import re

try:
    from jobhunter.navigation import main
except:
    from navigation import main
from rich.text import Text


def get_indeed_jobs(url):
    scraper = cloudscraper.create_scraper()
    page = scraper.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.find_all("div", "job_seen_beacon")
    return jobs


def scraper_indeed(skill, city, pages):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="cloudscraper")
    job_table = Table(title="Job Hunter")
    job_table.add_column("#", style="cyan")
    job_table.add_column("SALARY", style="cyan")
    job_table.add_column("TITLE", style="cyan")
    job_table.add_column("COMPANY", style="cyan")
    job_table.add_column("LOCATION", style="cyan")

    count = 1
    set_count = []
    for page in range(pages):
        url = (
                "https://www.indeed.com/jobs?q="
                + skill
                + "&l="
                + city
                + "&sort=date"
                + "&start="
                + str(page * 10)
        )

        get_indeed_jobs(url)
        jobs = get_indeed_jobs(url)

        for job in jobs:

            job_title = job.h2.text
            company_name = job.find("span", "companyName").text
            job_location = job.find("div", "companyLocation").text
            job_link = (
                    "https://www.indeed.com"
                    + job.find("h2", {"class": "jobTitle"}).find("a")["href"]
            )
            try:
                job_description = job.find("div", "job-snippet").text
            except AttributeError:
                job_description = ""

            job_salary = job.find("div", "salaryOnly").text
            salary_match = re.search(r'\$\d+(?:[,\s]\d+)*(?:\s*-\s*\$\d+(?:[,\s]\d+)*)?', job_salary)
            if salary_match:
                salary = re.sub(r"(\w)([A-Z])", r"\1 \2", salary_match.group(0))
            else:
                salary = ""

            record = (
                job_title,
                company_name,
                job_location,
                job_link,
                job_description,
                salary,
            )
            set_count.append(record)

            job_table.add_row(
                f"{count}",
                f"{job_salary}",
                f"{job_title}",
                f"{company_name}",
                f"{job_location}",
            )

            count += 1

    console = Console()
    console.print(job_table)
    text = Text()
    text.append("Would you like to see more details about a particular job?", style="bold blue")
    console.print(text)
    choice = Prompt.ask('> ',
                        choices=['y', 'n']).lower()
    if choice == "n":
        exit()
    if choice == "y":
        text = Text()
        text.append("Which job do you want details about? [Select #]", style="bold yellow")
        console.print(text)
        number = int(Prompt.ask("> "))
        posting = set_count[number - 1]

        table = Table(title=f"{posting[0]}")
        table.add_column("COMPANY NAME", style="cyan")
        table.add_column("LOCATION", style="cyan")
        table.add_column("DESCRIPTION", style="cyan")
        table.add_column("LINK", style="cyan")
        table.add_row(
            f"{posting[1]}", f"{posting[2]}", f"{posting[4]}", f"{posting[3]}"
        )

        console = Console()
        console.print(table)
        url = f"{posting[3]}"
        button = "#indeedApplyButton"
        selector = "//a[text()='Apply on company site']"
        text = Text()
        text.append("Would you like to apply to this job?", style="bold red")
        console.print(text)
        choice = Prompt.ask('> ',
                            choices=['y', 'n']).lower()
        if choice == "y":
            main(url, button, selector)
        if choice == "n":
            text = Text()
            text.append("Would you like go back to job listing?", style="bold red")
            console.print(text)
            choice = Prompt.ask('> ',
                                choices=['y', 'n']).lower()
            if choice == "y":
                for i in track(range(100), description='Searching Jobs....'):
                    time.sleep(0.02)
                scraper_indeed(skill, city, pages)
            if choice == "n":
                exit()
    return set_count


if __name__ == "__main__":
    scraper_indeed()
