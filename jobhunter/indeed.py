import requests
import cloudscraper
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table


def main():
    skill = input('Enter your Skill: ').strip()
    city = input('Enter the location: ').strip()
    pages = int(input('Enter the # of pages you want to search: '))

    table = Table(title='Job Hunter' )

    table.add_column("DATE", style="cyan")
    table.add_column("TITLE", style="cyan")
    table.add_column("COMPANY", style="cyan")
    table.add_column("LOCATION", style="cyan")

    for page in range (pages):
        scraper = cloudscraper.create_scraper()
        url = 'https://www.indeed.com/jobs?q=' + skill + '&l=' + city + '&sort=date' + '&start=' + str(page * 10)
        page = scraper.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        jobs = soup.find_all('div', 'job_seen_beacon')

        for job in jobs:
            job_title = job.h2.text
            company_name = job.find('span', 'companyName').text
            job_location = job.find('div', 'companyLocation').text
            job_link = 'https://www.indeed.com' + job.find('h2', {'class': 'jobTitle'}).find('a')['href']
            try:
                job_description = job.find('div', 'job-snippet').text
            except AttributeError:
                job_description = ''

            job_postdate = job.find('span', 'date').text
            try:
                job_salary = job.find('div', 'salaryOnly').text
            except AttributeError:
                job_salary = ''

            table.add_row(f'{job_postdate}', f'{job_title}', f'{company_name}', f'{job_location}')

        console = Console()
        console.print(table)

if __name__ == '__main__':
    main()