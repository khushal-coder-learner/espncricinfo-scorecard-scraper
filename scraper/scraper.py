from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from io import StringIO
import time, json

class EspnCricInfoScraper:

    def __init__(self, driver: webdriver.Chrome, wait_time: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    @staticmethod
    def create_chrome_driver(headless: bool = True):
        """
        Initializes and configures the Chrome WebDriver for scraping.

        Returns:
            WebDriver: Configured Selenium WebDriver instance.
        """
        options = Options()
        if headless:
            options.add_argument("--headless")  # Run without GUI
        options.add_argument("--disable-gpu")  # For safety in headless mode
        options.add_argument("--start-maximized")  # Ensures proper page rendering
        options.add_argument("user-agent=Mozilla/5.0 ... Chrome/125.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")  # Anti-bot detection

        return webdriver.Chrome(options=options)
    
    def load_page(self, url: str):
        self.driver.get(url)
        time.sleep(0.5)

    def handle_pop_up(self):
        """
        Handles and closes pop-ups if present.

        Args:
            driver (WebDriver): Active Selenium WebDriver instance.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.ID, "wzrk-cancel"))
            ).click()
        except Exception:
            pass  # No pop-up appeared

    def get_match_urls(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.ds-p-4')))

        matches_cards = self.driver.find_elements(By.CSS_SELECTOR, 'div.ds-p-4')
        matches_card = matches_cards[74]
        try:
            match_link_elems = matches_card.find_elements(By.XPATH, './/a[contains(@href, "/live-cricket-score")]')
        except NoSuchElementException:
            print("No links found")

        match_links = []
        match_names = []
        for link_elem in match_link_elems:
            try:
                href = link_elem.get_attribute('href').replace("/live-cricket-score", "/full-scorecard")
                match_name = link_elem.find_element(By.XPATH, './/span').text
            except NoSuchElementException:
                print("No link found")
            if href:
                match_links.append(href)
            if match_name:
                match_names.append(match_name)
                

        return match_links, match_names if match_names else []

    def extract_scorecard(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ds-mt-3')))
        except NoSuchElementException:
            print("No Such element found. ")



    def parse_scorecard(self):
        """
        Parses an ESPN Cricinfo full scorecard page into a clean, structured dictionary.
        Handles edge cases like Super Overs and No Result/Abandoned matches.
        """
        scorecard_dict = {"teams": {}, "match_info": {}}

        # Get HTML and parse all tables
        html = self.driver.page_source
        tables = pd.read_html(StringIO(html))

        # Extract team names from page headings
        team_names = self._extract_team_names()

        team_index = 0
        innings_tracker = None

        # Iterate through scorecard tables
        for table_idx, table in enumerate(tables):
            table.columns = [str(c).strip().lower().replace("\n", " ") for c in table.columns]
            table = table.dropna(how="all")  # Remove ds-hidden rows

            headers = table.columns.tolist()

            # Detect batting table
            if "r" in headers and "b" in headers and "sr" in headers:
                if team_index < len(team_names):
                    team_name = team_names[team_index]
                else:
                    # Super Over case: assign custom name
                    team_name = f"Super Over {team_index - len(team_names) + 1}"

                team_name, team_index = self._process_batting_table(
                    table,
                    team_name,         # pass the resolved name directly
                    scorecard_dict,
                    team_index,
                    table_idx
                )
                innings_tracker = team_name

            # Detect bowling table
            elif "o" in headers and "m" in headers and "econ" in headers:
                if innings_tracker:
                    self._process_bowling_table(table, scorecard_dict, innings_tracker)

        # Parse match info panel
        self._process_match_info(scorecard_dict)

        # Handle No Result/Abandoned case
        try:
            status_elem = self.driver.find_element(
                By.CSS_SELECTOR,
                "p.ds-text-tight-m.ds-font-regular.ds-truncate.ds-text-typo"
            )
            match_status = status_elem.text.strip().lower()
            if "no result" in match_status or "abandoned" in match_status:
                scorecard_dict["match_info"]["status"] = match_status
        except NoSuchElementException:
            pass

        return scorecard_dict


    # =========================
    # Extractors
    # =========================

    def _extract_team_names(self):
        """Gets the team names from the scorecard page."""
        return [
            el.text.strip() for el in self.driver.find_elements(
                By.CSS_SELECTOR,
                "div.ds-rounded-lg.ds-mb-2 span.ds-text-title-xs.ds-font-bold.ds-capitalize"
            )
        ]


    # =========================
    # Batting
    # =========================

    def _process_batting_table(self, table, team_name, scorecard_dict, team_index, table_idx):
        """
        Processes a single batting table (including normal innings and Super Overs).
        """
        scorecard_dict["teams"][team_name] = {}

        headers = table.columns.tolist()
        batting_rows = []
        extras_row = None
        total_row = None

        # Identify rows dynamically (but skip DNB and FOW here)
        for _, row in table.iterrows():
            first_cell = str(row[headers[0]]).strip()

            if first_cell.lower().startswith("extras"):
                extras_row = row
            elif first_cell.lower().startswith("total"):
                total_row = row
            elif first_cell.lower().startswith("fall of wickets") or first_cell.lower().startswith("did not bat"):
                # handled separately using Selenium
                continue
            else:
                batting_rows.append(row)

        # Parse batting table data
        scorecard_dict["teams"][team_name]["batting"] = self._parse_batting_rows(pd.DataFrame(batting_rows), headers)
        if extras_row is not None:
            scorecard_dict["teams"][team_name]["extras"] = self._parse_extras_row(extras_row, headers)
        if total_row is not None:
            scorecard_dict["teams"][team_name]["total"] = self._parse_total_row(total_row, headers)

        # Parse Fall of Wickets using Selenium
        scorecard_dict["teams"][team_name]["fall_of_wickets"] = self._parse_fow_row(table_idx)

        return team_name, team_index + 1

    def _parse_batting_rows(self, batting_rows, headers):
        batting_list = []
        for _, row in batting_rows.iterrows():
            # Handle strike rate safely
            sr_value = row["sr"]
            try:
                strike_rate = float(sr_value)
            except (ValueError, TypeError):
                strike_rate = 0.0

            def safe_int(val):
                try:
                    return int(val)
                except (ValueError, TypeError):
                    return 0

            batting_list.append({
                "batsman": row[headers[0]],
                "dismissal": row[headers[1]],
                "runs": safe_int(row["r"]),
                "balls": safe_int(row["b"]),
                "fours": safe_int(row.get("4s", 0)),
                "sixes": safe_int(row.get("6s", 0)),
                "strike_rate": strike_rate
            })
        return batting_list


    def _parse_extras_row(self, extras_row, headers):
        def safe_int(val):
            try:
                return int(val)
            except (ValueError, TypeError):
                return 0

        return {
            "total": safe_int(extras_row.get("r", 0)),
            "detail": extras_row[headers[1]]
        }


    def _parse_total_row(self, total_row, headers):
        return {
            "runs": str(total_row.get("r", "0")),   # keep as string like "174/8"
            "detail": total_row[headers[1]]
        }
    

    def _parse_fow_row(self, table_idx):
        """
        Extracts 'Fall of Wickets' info from spans scoped to a specific batting table.
        """
        fow_list = []
        try:
            # Locate the specific table block using table_idx
            table_blocks = self.driver.find_elements(By.CSS_SELECTOR, "div.ds-rounded-lg.ds-mb-2")
            if table_idx < len(table_blocks):
                fow_row = table_blocks[table_idx].find_element(By.XPATH, ".//tr[.//strong[contains(text(),'Fall of wickets')]]")
                spans = fow_row.find_elements(By.TAG_NAME, "span")
                for sp in spans:
                    text = sp.text.strip()
                    if "(" not in text:
                        continue
                    score = text.split("(")[0].strip()
                    details = text.split("(")[1].replace(")", "").split(",")
                    player = details[0].strip()
                    over = details[1].replace("ov", "").strip() if len(details) > 1 else ""
                    fow_list.append({"score": score, "player": player, "over": over})
        except NoSuchElementException:
            pass
        return fow_list


    # =========================
    # Bowling
    # =========================

    def _process_bowling_table(self, table, scorecard_dict, team_name):
        headers = table.columns.tolist()
        bowling_list = []

        for _, row in table.iterrows():
            try:
                overs = float(str(row["o"]).replace(".", "", 1))  # try numeric
                maidens = int(row["m"])
                runs = int(row["r"])
                wickets = int(row["w"])
                economy = float(row["econ"])
            except ValueError:
                # If any conversion fails, it's a commentary row → skip it
                continue

            bowling_list.append({
                "bowler": row[headers[0]],
                "overs": row["o"],
                "maidens": row["m"],
                "runs": row["r"],
                "wickets": row["w"],
                "economy": row["econ"]
            })

        scorecard_dict["teams"][team_name]["bowling"] = bowling_list



    # =========================
    # Match Info
    # =========================

    def _process_match_info(self, scorecard_dict):
        def normalize_label(label):
            label = label.lower()
            label = label.replace("(", "").replace(")", "")
            label = label.replace("-", "_")
            label = "_".join(label.split())  # collapse spaces into underscores
            return label.strip("_")

        match_info_rows = self.driver.find_elements(By.CSS_SELECTOR, "table.ds-table tr")
        for row in match_info_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                raw_label = cells[0].text.strip()
                value = cells[1].text.strip().replace("\n", " ")

                label = normalize_label(raw_label)

                # Special handling for replacements
                if "impact player" in raw_label.lower() and "rcb" in value.lower():
                    label = "rcb_player_replacement"
                elif "impact player" in raw_label.lower() and "kkr" in value.lower():
                    label = "kkr_player_replacement"

                scorecard_dict["match_info"][label] = value


    
    def save_to_json(self, scorecard, match_name):
        with open(f"data/{match_name}.json", 'w', encoding='utf-8') as f:
            json.dump(scorecard, f, indent=4, ensure_ascii=False)



    
