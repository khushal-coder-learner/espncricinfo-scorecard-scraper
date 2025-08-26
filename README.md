Cricinfo Scorecard Scraper 🏏

A Selenium-based scraper that extracts full scorecards from ESPNcricinfo and structures them into clean JSON.
This project is built for educational purposes only — it’s not affiliated with or endorsed by ESPN.

✨ Features (Current)

Scrapes batting & bowling tables from completed matches.

Captures strike rate, boundaries, extras, totals, fall of wickets.

Handles Super Overs and extra innings.

Saves structured data to JSON files.

📊 Example Output

Here’s a snippet from DC vs RR – 32nd Match, IPL 2025
:

{
  "teams": {
    "Delhi Capitals": {
      "batting": [
        {
          "batsman": "Tristan Stubbs",
          "dismissal": "not out",
          "runs": 34,
          "balls": 18,
          "fours": 2,
          "sixes": 2,
          "strike_rate": 188.88
        }
      ],
      "extras": { "total": 9, "detail": "(lb 1, nb 1, w 7)" },
      "total": { "runs": "188/5", "detail": "20 Ov (RR: 9.40)" }
    }
  },
  "match_info": {
    "toss": "Rajasthan Royals, elected to field first",
    "series": "Indian Premier League",
    "season": "2025",
    "player_of_the_match": "Mitchell Starc"
  }
}


More outputs:

RCB vs KKR – 58th Match (buggy)

RCB vs PBKS – Final

🚧 Known Issues (Help Wanted!)

get_match_urls() currently assumes 74 IPL matches → needs generalization.

Some matches (e.g. RCB vs KKR) scrape player roles instead of scorecards.

NaN values appear in Super Over totals/extras.

Bowling names inconsistent (abbreviated vs full).

Missing fall of wickets in some innings.

Check out Issues
 to contribute.

🔧 Installation & Usage
git clone https://github.com/<your-username>/cricscraper.git
cd cricscraper

# Create venv & install deps
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt

# Run scraper (example)
python -m cricscraper --url "https://www.espncricinfo.com/series/ipl-2025-1410349/delhi-capitals-vs-rajasthan-royals-32nd-match-1410379/full-scorecard"


Outputs will be saved under data/ as JSON.

📅 Roadmap

 Generalize match URL extraction (beyond IPL 2025).

 Clean up Super Over parsing.

 Normalize player/bowler names.

 Add Excel/CSV export with formatting.

 Add retries, backoff, and caching.

🤝 Contributing

Fork → branch → PR.

Open Issues
 for bugs/ideas.

Check CONTRIBUTING.md
.

⚖️ Disclaimer

This project is purely for educational and personal learning.
All trademarks, names, and logos belong to their respective owners.