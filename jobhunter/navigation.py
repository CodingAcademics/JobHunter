import time
from playwright.sync_api import sync_playwright
import sys
from rich.prompt import Prompt
from rich.panel import Panel


def main(url, button, selector):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)
        apply_button = page.query_selector(button)
        if apply_button:
            apply_button.click()
        else:
            apply_button = page.query_selector(button)
            if not apply_button:
                apply_button = page.query_selector(selector)
            if apply_button:
                apply_button.click()
            print('Do you want to exit program?')
            choice = Prompt.ask('> ',
                                choices=['y', 'n']).lower()
            if choice == "y":
                sys.exit()
            if choice == "n":
                browser = p.firefox.launch(headless=False, slow_mo=1000)
                page = browser.new_page()
                page.goto(url)
                apply_button = page.query_selector(button)
                if apply_button:
                    apply_button.click()
                else:
                    apply_button = page.query_selector(button)
                    if not apply_button:
                        apply_button = page.query_selector(selector)
                    if apply_button:
                        apply_button.click()
                        sys.exit()
        time.sleep(300)
    browser.close()
