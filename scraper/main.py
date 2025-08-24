from scraper.scraper import EspnCricInfoScraper
import json, time


if __name__ == '__main__':
    driver = EspnCricInfoScraper.create_chrome_driver(headless=False)
    scraper = EspnCricInfoScraper(driver, wait_time=10)

    try:
        url = "https://www.espncricinfo.com/series/ipl-2025-1449924/match-schedule-fixtures-and-results"
        scraper.load_page(url)
        print(f"Loading {url} ...")

        scraper.handle_pop_up()

        print("Extracting match urls ...")
        match_links, match_names = scraper.get_match_urls()

        for link, match_name in zip(match_links, match_names):

            print(f"Loading match: {match_name}")
            scraper.load_page(link)
            scraper.extract_scorecard()
            print("Found Scorecard")
            scorecard = scraper.parse_scorecard()
            print("Parsed Scorecard")
            scraper.save_to_json(scorecard, match_name)
            print("Saved to Json")
        else:
            print("Failed to scrape.")

    finally:
        driver.quit()
