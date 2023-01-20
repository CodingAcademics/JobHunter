# import pytest
from jobhunter.indeed import scraper_indeed
from jobhunter.zip_recruiter import scraper_zip_recruiter
# from jobhunter.interface import search_job, welcome, your_job
# from navigation import main


def test_scraper_indeed():
    # Test a basic search for software developer jobs in New York City
    skill = "software developer"
    city = "New York City"
    pages = 2
    result = scraper_indeed(skill, city, pages)

    # Check that the correct number of rows are returned
    assert len(result) == 20

    # Check that the first row contains the expected data
    assert result[0][0] == "Software Developer"
    assert result[0][1] == "Example Company"
    assert result[0][2] == "New York City, NY"
    assert result[0][3] == "https://www.indeed.com/job_link"
    assert result[0][4] == "Job description text."
    assert result[0][5] == ""


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
