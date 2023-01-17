import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient
from rich.console import Console
from rich.table import Table


# environment variable
def configure():
    load_dotenv()


def main():
    configure()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"}

    client = ScrapingBeeClient(os.getenv('api_key'))

    # Skills & Place of Work
    skill = input('Enter your Skill: ').strip()
    city = input('Enter the location: ').strip()
    pages = int(input('Enter the # of pages you want to search: '))

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
            description = card.find('p', 'job_snippet').text.strip() if card.find('p', 'job_snippet') else None
            salary = card.find('div', 'value').text.strip() if card.find('div', 'value') else None
            apply = card.find('div', {'class': 'job_actions'}).find('a')['href'] if card.find('div', {
                'class': 'job_actions'}).find('a') else None

            table = Table(title='Job Hunter')

            table.add_column("DATES", style="cyan")
            table.add_column()
            table.add_column()

            table.add_row("")
            table.add_row()
            table.add_row()

            console = Console()
            console.print(table)

            # if title:
            #     print(f'JOB TITLE: {title}')
            # if location:
            #     print(f'CITY: {location}')
            # if description:
            #     print(f'SUMMARY: {description}')
            # if salary:
            #     print(f'PAY RATE: {salary}')
            # if apply:
            #     print(f'CLICK TO APPLY: {apply}')
            #
            # else:
            #     print('I got nothing for you.')


if __name__ == '__main__':
    main()
