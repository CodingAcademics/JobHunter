import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient


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
        url = 'https://www.simplyhired.com/search?' + skill + \
              '&l=' + city + '&sort=date' + '&start=' + str(page * 10)
        # Get request to indeed with headers above
        response = client.get(url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('div', 'SerpJob-jobCard card isp')

        for card in cards:
            title = card.h3.text.strip() if card.h3 else None
            location = card.find('span', 'jobposting-location').text.strip() if card.find('span', 'jobposting-location') else None
            description = card.find('p', 'jobposting-snippet').text.strip() if card.find('p', 'jobposting-snippet') else None
            salary = card.find('div', 'jobposting-salary SerpJob-salary').text.strip() if card.find('div', 'jobposting-salary SerpJob-salary') else None
            apply = 'https://www.simplyhired.com' + card.find('h3', {'class': 'jobposting-title'}).find('a')['href'] if card.find('h3', {'class': 'jobposting-title'}).find('a') else None
            if title:
                print(f'JOB TITLE: {title}')
            if location:
                print(f'CITY: {location}')
            if description:
                print(f'SUMMARY: {description}')
            if salary:
                print(f'PAY RATE: {salary}')
            if apply:
                print(f'CLICK TO APPLY: {apply}')

            else:
                print('I got nothing for you.')


if __name__ == '__main__':
    main()