from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1"
                        "&pageNum=0")

        await page.wait_for_timeout(1000)

        title_element = await page.query_selector("title")
        title_text = await title_element.inner_text()
        print(title_text)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
