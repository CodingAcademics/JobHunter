# import os
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
  browser = playwright.chromium.launch(headless=False)
  # app_data_path = os.getenv("LOCALAPPDATA")
  # user_data_path = os.path.join(app_data_path, 'Chromium\\USER DATA\\Default')
  # context = playwright.chromium.launch_persistent_context(user_data_path, headless=False)
  context = browser.new_context()
  page = context.new_page()

  page.goto("https://www.google.com/")
  # page.wait_for_timeout(5000)

with sync_playwright() as playwright:
  run(playwright)

    # if wsl wslview platform.system()
    # if 'Linux' run wslview $url
    # if 'Darwin'open Url
    # if mac open()

# """
# >>> import os
# >>> os.name
# 'posix'
# >>> import platform
# >>> platform.system()
# 'Linux'
# >>>

# """
