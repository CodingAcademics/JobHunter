# import pyfiglet

# def play():
#    print(pyfiglet.figlet_format("Welcome to\nJob Hunter", font="slant", justify="center"))
#    # width = 200 style="light_steel_blue"
#    print("(y)es to begin hunter or (n)o to decline")
#    choice = input("> ")
#    return choice == "y"


# def decline_game():
#    print("OK. Maybe another time")


# if __name__ == '__main__':
#    play()

import asyncio
import json
import re
from typing import List
from urllib.parse import urlencode

from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient


def parse_search_page(result):
    data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', result.content)
    data = json.loads(data[0])
    return {
        "results": data["metaData"]["mosaicProviderJobCardsModel"]["results"],
        "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
    }


async def scrape_search(client: ScrapflyClient, query: str, location: str):
    def make_page_url(offset):
        parameters = {"q": query, "l": location, "filter": 0, "start": offset}
        return "https://www.indeed.com/jobs?" + urlencode(parameters)

    print(f"scraping first page of search: {query=}, {location=}")
    result_first_page = await client.async_scrape(
        ScrapeConfig(
            make_page_url(0),
            country="US",
            asp=True,
        )
    )
    data_first_page = parse_search_page(result_first_page)

    results = data_first_page["results"]
    total_results = sum(category["jobCount"] for category in data_first_page["meta"])
    # there's a page limit on indeed.com
    if total_results > 1000:
        total_results = 1000

    print(f"scraping remaining {total_results - 10 / 10} pages")
    other_pages = [
        ScrapeConfig(url=make_page_url(offset), country="US", asp=True) for offset in range(10, total_results + 10, 10)
    ]
    async for result in client.concurrent_scrape(other_pages):
        try:
            data = parse_search_page(result)
            results.extend(data["results"])
        except Exception as e:
            print(e)
    return results


def parse_job_page(result: ScrapeApiResponse):
    """parse job data from job listing page"""
    data = re.findall(r"_initialData=(\{.+?\});", result.content)
    data = json.loads(data[0])
    return data["jobInfoWrapperModel"]["jobInfoModel"]


async def scrape_jobs(client: ScrapflyClient, job_keys: List[str]):
    """scrape job page"""
    urls = [f"https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk={job_key}" for job_key in job_keys]
    scraped = []
    async for result in client.concurrent_scrape([ScrapeConfig(url=url, country="US", asp=True) for url in urls]):
        scraped.append(parse_job_page(result))
    return scraped


async def main():
    with ScrapflyClient(key="scp-live-510ad01bc6ee466cac724a1d53a150d9", max_concurrency=2) as client:
        search_results = await scrape_search(client, "python", "Texas")
        print(json.dumps(search_results, indent=2))
        _found_job_ids = [result["jobkey"] for result in search_results]
        job_results = await scrape_jobs(client, job_keys=_found_job_ids[:10])
        print(json.dumps(job_results, indent=2))


asyncio.run(main())
