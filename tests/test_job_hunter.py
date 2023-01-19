# import pytest
# from jobhunter.indeed import scraper_indeed, job_table, table
#
#
# def test_scraper_indeed():
#     # Call the scraper_indeed function with sample skill, city, and pages
#     scraper_indeed("Python", "San Francisco", 2)
#     # Assert that the output table has the expected number of rows
#     assert len(job_table.rows) == 20
#     # Assert that the first row of the table has the expected values
#     assert job_table.rows[0][0] == "#"
#     assert job_table.rows[0][1] == "DATE"
#     assert job_table.rows[0][2] == "TITLE"
#     assert job_table.rows[0][3] == "COMPANY"
#     assert job_table.rows[0][4] == "LOCATION"
#     # Assert that the second row of the table has the expected values
#     assert job_table.rows[1][0] == "1"
#     assert job_table.rows[1][1] == "job_postdate"
#     assert job_table.rows[1][2] == "job_title"
#     assert job_table.rows[1][3] == "company_name"
#     assert job_table.rows[1][4] == "job_location"
#     # Assert that the output table has the expected number of rows
#     assert len(table.rows) == 1
#     # Assert that the first row of the table has the expected values
#     assert table.rows[0][0] == "COMPANY NAME"
#     assert table.rows[0][1] == "LOCATION"
#     assert table.rows[0][2] == "DESCRIPTION"
#     assert table.rows[0][3] == "LINK"
#     assert table.rows[1][0] == "posting[1]"
#     assert table.rows[1][1] == "posting[2]"
#     assert table.rows[1][2] == "posting[4]"
#     assert table.rows[1][3] == "posting[3]"


