import pytest
from dotenv import load_dotenv

from jobhunter.indeed import get_indeed_jobs
from jobhunter.simplyhired import get_simple_hired_jobs
from jobhunter.zip_recruiter import get_zip_recruiter_jobs


def test_get_indeed_jobs():
    with pytest.warns(DeprecationWarning):
        skill = "python"
        city = "seattle"
        page = 1
        url = (
                "https://www.indeed.com/jobs?q="
                + skill
                + "&l="
                + city
                + "&sort=date"
                + "&start="
                + str(page * 10)
        )
        assert len(get_indeed_jobs(url)) > 0


def test_get_simple_hired_jobs():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"
    }
    skill = "python"
    city = "seattle"
    page = 1
    url = (
            "https://www.simplyhired.com/search?"
            + "q="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_simple_hired_jobs(url, headers)) > 0


def test_get_zip_recruiter_jobs():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
        "Safari/537.36"
    }
    skill = "python"
    city = "seattle"
    page = 1
    url = (
            "https://www.ziprecruiter.com/jobs-search?search="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_zip_recruiter_jobs(url, headers)) > 0


def test_get_indeed_jobs_san_fran():
    with pytest.warns(DeprecationWarning):
        skill = "junior developer"
        city = "san francisco"
        page = 2
        url = (
                "https://www.indeed.com/jobs?q="
                + skill
                + "&l="
                + city
                + "&sort=date"
                + "&start="
                + str(page * 10)
        )
        assert len(get_indeed_jobs(url)) > 0


def test_get_simple_hired_jobs_san_fran():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"
    }
    skill = "junior developer"
    city = "san francisco"
    page = 1
    url = (
            "https://www.simplyhired.com/search?"
            + "q="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_simple_hired_jobs(url, headers)) > 0


def test_get_zip_recruiter_jobs_san_fran():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
        "Safari/537.36"
    }
    skill = "junior developer"
    city = "san francisco"
    page = 1
    url = (
            "https://www.ziprecruiter.com/jobs-search?search="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_zip_recruiter_jobs(url, headers)) > 0


def test_get_indeed_jobs_senior_austin():
    with pytest.warns(DeprecationWarning):
        skill = "senior developer"
        city = "austin"
        page = 2
        url = (
                "https://www.indeed.com/jobs?q="
                + skill
                + "&l="
                + city
                + "&sort=date"
                + "&start="
                + str(page * 10)
        )
        assert len(get_indeed_jobs(url)) > 0


def test_get_simple_hired_jobs_senior_austin():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
                      "Safari/537.36"
    }
    skill = "senior developer"
    city = "austin"
    page = 1
    url = (
            "https://www.simplyhired.com/search?"
            + "q="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_simple_hired_jobs(url, headers)) > 0


def test_get_zip_recruiter_jobs_senior_austin():
    load_dotenv()
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 "
        "Safari/537.36"
    }
    skill = "senior developer"
    city = "austin"
    page = 1
    url = (
            "https://www.ziprecruiter.com/jobs-search?search="
            + skill
            + "&l="
            + city
            + "&sort=date"
            + "&start="
            + str(page * 10)
    )
    assert len(get_zip_recruiter_jobs(url, headers)) > 0
