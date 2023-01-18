import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient
from rich.console import Console
from rich.table import Table


# environment variable
def configure():
    load_dotenv()


def scraper_zip_recruiter(skill, city, pages):
    configure()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"}

    client = ScrapingBeeClient(os.getenv('api_key'))

    table = Table(title='Job Hunter')

    table.add_column("SALARY", style="cyan")
    table.add_column("TITLE", style="cyan")
    table.add_column("COMPANY", style="cyan")
    table.add_column("LOCATION", style="cyan")

    for page in range(pages):
        client = ScrapingBeeClient(os.getenv('api_key'))
        # Connecting to zip recruiter
        url = 'https://www.ziprecruiter.com/jobs-search?search=' + skill + \
              '&l=' + city + '&sort=date' + '&start=' + str(page * 10)

        # Get request to indeed with headers above
        response = client.get(url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('article', 'new_job_item job_item')

        for card in cards:
            title = card.h2.text.strip() if card.h2 else None
            location = card.find('a', 'company_location').text.strip() if card.find('a', 'company_location') else None
            company_name = card.find('div', 'company_name_row').text.strip() if card.find('div', 'company_name_row') else None
            description = card.find('p', 'job_snippet').text.strip() if card.find('p', 'job_snippet') else None
            salary = card.find('div', 'value').text.strip() if card.find('div', 'value') else None
            apply = card.find('div', {'class': 'job_actions'}).find('a')['href'] if card.find('div', {
                'class': 'job_actions'}).find('a') else None

            table.add_row(f'{salary}', f'{title}', f'{company_name}', f'{location}')

    console = Console()
    console.print(table)


if __name__ == '__main__':
    scraper_zip_recruiter()
