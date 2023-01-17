import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient
from rich.console import Console
from rich.table import Table


# environment variable
def configure():
    load_dotenv()


def scraper_simply_hired(skill, city, pages):
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
        url = 'https://www.simplyhired.com/search?' + skill + \
              '&l=' + city + '&sort=date' + '&start=' + str(page * 10)
        # Get request to indeed with headers above
        response = client.get(url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('div', 'SerpJob-jobCard card isp')

        for card in cards:
            title = card.h3.text.strip() if card.h3 else None
            location = card.find('span', 'jobposting-location').text.strip() if card.find('span',
                                                                                          'jobposting-location') else None
            description = card.find('p', 'jobposting-snippet').text.strip() if card.find('p',
                                                                                         'jobposting-snippet') else None
            company_name = card.find('h3', 'jobposting-title').text.strip() if card.find('h3',
                                                                                         'jobposting-title') else None
            salary = card.find('div', 'jobposting-salary SerpJob-salary').text.strip() if card.find('div',
                                                                                                    'jobposting-salary SerpJob-salary') else None
            apply = 'https://www.simplyhired.com' + card.find('h3', {'class': 'jobposting-title'}).find('a')[
                'href'] if card.find('h3', {'class': 'jobposting-title'}).find('a') else None

            table.add_row(f'{salary}', f'{title}', f'{company_name}', f'{location}')

        console = Console()
        console.print(table)


if __name__ == '__main__':
    scraper_simply_hired()
