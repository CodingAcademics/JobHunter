# import pytest
from jobhunter.indeed import scraper_indeed
# from jobhunter.zip_recruiter import scraper_zip_recruiter
# from rich.text import Text
# from jobhunter.interface import search_job, welcome, your_job
# from navigation import main


def test_scraper_indeed(set_count=None):
    scraper_indeed("python", "New York", 2)
    # Check if the output contains the expected number of jobs (20)
    assert len(set_count) == 20
    # Check if the output contains the expected job title
    assert set_count[0][0] == "Python Developer"
    # Check if the output contains the expected company name
    assert set_count[0][1] == "ABC Company"
    # Check if the output contains the expected location
    assert set_count[0][2] == "New York, NY"


def test_scraper_zip_recruiter():
    # Test that the function is able to scrape job listings
    # skill = "python"
    # city = "seattle"
    # pages = 1
    # scraper_indeed(skill, city, pages)
    # assert len(set_count) > 0
    pass


def test_simply_hired():
    # # Test that the function is able to scrape job listings
    # skill = "python"
    # city = "seattle"
    # pages = 1
    # scraper_indeed(skill, city, pages)
    # assert len(set_count) > 0
    pass


def test_search_job():
    pass


def test_welcome():
    pass


def test_your_job():
    pass
