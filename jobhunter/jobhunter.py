from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup
import re


def main():
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"}

    client = ScrapingBeeClient(
        api_key='C3PV0GKBFWRXZLUSC71E83Y43YL0UDXG0O14RISX275W2C5PN7YOI68KT3TZKDD01DWOLGJEMB81409C')

    # Skills & Place of Work
    skill = input('Enter your Skill: ').strip()
    city = input('Enter the location: ').strip()
    pages = int(input('Enter the # of pages you want to search: '))

    for page in range(pages):
        client = ScrapingBeeClient(
            api_key='C3PV0GKBFWRXZLUSC71E83Y43YL0UDXG0O14RISX275W2C5PN7YOI68KT3TZKDD01DWOLGJEMB81409C')
        # Connecting to zip recruiter
        url = 'https://www.ziprecruiter.com/jobs-search?search=' + skill + \
              '&l=' + city + '&sort=date' + '&start=' + str(page * 10)

        # Get request to indeed with headers above
        response = client.get(url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('article', 'new_job_item job_item')

        for card in cards:
            title = card.h2.text.strip()
            location = card.find('a', 'company_location').text.strip()
            description = card.find('p', 'job_snippet').text.strip()
            salary = card.find('div', 'value').text.strip()
            apply = card.find('div', {'class': 'job_actions'}).find('a')['href']
            print(f'JOB TITLE: {title}')
            print(f'CITY: {location}')
            print(f'SUMMARY: {description}')
            print(f'PAY RATE: {salary}')
            print(f'CLICK TO APPLY: {apply}')


if __name__ == '__main__':
    main()
