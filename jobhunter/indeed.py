import requests
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
url = 'https://www.indeed.com/jobs?q=python+developer&l=Seattle%2C+WA&from=searchOnHP&vjk=d4681e480323b495'
page = scraper.get(url)
soup = BeautifulSoup(page.content, "html.parser")
# soup = BeautifulSoup(page.content, 'html.parser
jobs = soup.find_all('div', 'job_seen_beacon')
job = jobs[0]


def get_record(job):
    job_title = job.h2.text
    company_name = job.find('span', 'companyName').text
    job_location = job.find('div', 'companyLocation').text
    job_link = 'https://www.indeed.com' + job.find('h2', {'class': 'jobTitle'}).find('a')['href']
    print(job_link)
    try:
        job_description = job.find('div', 'job-snippet').text
    except AttributeError:
        job_description = ''

    job_postdate = job.find('span', 'date').text
    try:
        job_salary = job.find('div', 'salaryOnly').text
    except AttributeError:
        job_salary = ''

    record = (job_title, company_name, job_salary, job_location, job_description, job_postdate)

    return record


records = []

for job in jobs:
    posting = get_record(job)
    records.append(posting)

print(records[0])
while True:
    try:
        url = 'https://www.indeed.com/jobs?q=python+developer&l=Seattle%2C+WA&from=searchOnHP&vjk=d4681e480323b495'  + soup.find('a', {'aria-label': 'Next'}).get('href')
    except AttributeError:
        break

    response = scraper.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', 'job_seen_beacon')

    for job in jobs:
        posting = get_record(job)
        records.append(posting)

print(len(records))