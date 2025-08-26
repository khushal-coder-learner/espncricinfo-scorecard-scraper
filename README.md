# ESPNCricinfo Scorecard Scraper 🏏

A Selenium-based scraper that extracts **full scorecards** from ESPNcricinfo and structures them into clean JSON.
This project is built **for educational purposes only** — it’s not affiliated with or endorsed by ESPN.

---

## ✨ Features (Current)

* Scrapes **batting & bowling tables** and **match details** from completed matches.
* Captures **strike rate, boundaries, extras, totals, fall of wickets**.
* Handles **Super Overs** and extra innings.
* Saves structured data to JSON files.

---

## 📊 Example Output

Here’s a snippet from [DC vs RR – 32nd Match, IPL 2025](espncricinfo-scorecard-scraper\data\DC vs RR - 32nd Match.json):

```json
 "teams": {
        "Delhi Capitals": {
            "batting": [
                {
                    "batsman": "Jake Fraser-McGurk",
                    "dismissal": "c Jaiswal b Archer",
                    "runs": 9,
                    "balls": 6,
                    "fours": 2,
                    "sixes": 0,
                    "strike_rate": 150.0
                },
                {
                    "batsman": "Abishek Porel",
                    "dismissal": "c Parag b Hasaranga",
                    "runs": 49,
                    "balls": 37,
                    "fours": 5,
                    "sixes": 1,
                    "strike_rate": 132.43
                },
                {
                    "batsman": "Karun Nair",
                    "dismissal": "run out (Hasaranga/Sandeep Sharma)",
                    "runs": 0,
                    "balls": 3,
                    "fours": 0,
                    "sixes": 0,
                    "strike_rate": 0.0
                },
                {
                    "batsman": "KL Rahul †",
                    "dismissal": "c Hetmyer b Archer",
                    "runs": 38,
                    "balls": 32,
                    "fours": 2,
                    "sixes": 2,
                    "strike_rate": 118.75
                },
                {
                    "batsman": "Tristan Stubbs",
                    "dismissal": "not out",
                    "runs": 34,
                    "balls": 18,
                    "fours": 2,
                    "sixes": 2,
                    "strike_rate": 188.88
                },
                {
                    "batsman": "Axar Patel (c)",
                    "dismissal": "c Jurel b Theekshana",
                    "runs": 34,
                    "balls": 14,
                    "fours": 4,
                    "sixes": 2,
                    "strike_rate": 242.85
                },
                {
                    "batsman": "Ashutosh Sharma",
                    "dismissal": "not out",
                    "runs": 15,
                    "balls": 11,
                    "fours": 2,
                    "sixes": 0,
                    "strike_rate": 136.36
                }
            ],
            "extras": {
                "total": 9,
                "detail": "(lb 1, nb 1, w 7)"
            },
            "total": {
                "runs": "188/5",
                "detail": "20 Ov (RR: 9.40)"
            },
            "fall_of_wickets": [
                {
                    "score": "1-34",
                    "player": "Jake Fraser-McGurk",
                    "over": "2.3"
                },
                {
                    "score": "2-34",
                    "player": "Karun Nair",
                    "over": "3.1"
                },
                {
                    "score": "3-97",
                    "player": "KL Rahul",
                    "over": "12.4"
                },
                {
                    "score": "4-105",
                    "player": "Abishek Porel",
                    "over": "13.5"
                },
                {
                    "score": "5-146",
                    "player": "Axar Patel",
                    "over": "16.6"
                }
            ],
            "bowling": [
                {
                    "bowler": "Jofra Archer",
                    "overs": "4",
                    "maidens": "0",
                    "runs": "32",
                    "wickets": "2",
                    "economy": "8.00"
                },
                {
                    "bowler": "Tushar Deshpande",
                    "overs": "3",
                    "maidens": "0",
                    "runs": "38",
                    "wickets": "0",
                    "economy": "12.66"
                },
                {
                    "bowler": "Sandeep Sharma",
                    "overs": "4",
                    "maidens": "0",
                    "runs": "33",
                    "wickets": "0",
                    "economy": "8.25"
                },
                {
                    "bowler": "Maheesh Theekshana",
                    "overs": "4",
                    "maidens": "0",
                    "runs": "40",
                    "wickets": "1",
                    "economy": "10.00"
                },
                {
                    "bowler": "Wanindu Hasaranga",
                    "overs": "4",
                    "maidens": "0",
                    "runs": "38",
                    "wickets": "1",
                    "economy": "9.50"
                },
                {
                    "bowler": "Riyan Parag",
                    "overs": "1",
                    "maidens": "0",
                    "runs": "6",
                    "wickets": "0",
                    "economy": "6.00"
                }
            ]
        },
"match_info": {
        "toss": "Rajasthan Royals, elected to field first",
        "series": "Indian Premier League",
        "season": "2025",
        "player_of_the_match": "Mitchell Starc",
        "hours_of_play_local_time": "19.30 start, First Session 19.30-21.00, Interval 21.00-21.20, Second Session 21.20-22.50",
        "match_days": "16 April 2025 - night (20-over match)",
        "dc_player_replacement": "Impact player:  Mukesh Kumar in,  Abishek Porel  out (1st innings, 19.6 ov)",
        "rr_player_replacement": "Impact player:  Shubham Dubey in,  Maheesh Theekshana  out (2nd innings, 0.5 ov)",
        "umpires": "Akshay Totre DRS Keyur Kelkar DRS",
        "tv_umpire": "Rohan Pandit",
        "reserve_umpire": "Anish Sahasrabudhe",
        "match_referee": "Shakti Singh",
        "points": "Delhi Capitals 2, Rajasthan Royals 0",
        "extras": "(b 1, lb 1, nb 1, w 3)",
        "total": "188(4 wkts; 20 ovs)"
    }
}
```

More outputs:

* [RCB vs KKR – 58th Match (buggy)]("espncricinfo-scorecard-scraper\data\RCB vs KKR - 58th Match.json")
* [RCB vs PBKS – Final](espncricinfo-scorecard-scraper\data\RCB vs PBKS - Final.json)

---

## 🚧 Known Issues (Help Wanted!)

* `get_match_urls()` currently assumes **74 IPL matches** → needs generalization.
* `NaN` values appear in Super Over totals/extras.
* Buggy bowling table extraction
* Missing **fall of wickets** in some innings.

Check out [Issues](../../issues) to contribute.

---

## 🔧 Installation & Usage

```bash
git clone https://github.com/khushal-coder-learner/espncricinfo-scorecard-scraper.git
cd espncricinfo-scorecard-scraper

# Create venv & install deps
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt

# Run scraper 
python -m scraper.main
```

Outputs will be saved under `data/` as JSON.

---

## 📅 Roadmap

* [ ] Generalize match URL extraction (beyond IPL 2025).
* [ ] Clean up **Super Over parsing**.
* [ ] Fix missing or repeated bowling tables.
* [ ] Fix missing fall of wickets.
* [ ] Add Excel/CSV export with formatting.
* [ ] Add retries, backoff, and caching.

---

## 🤝 Contributing

* Fork → branch → PR.
* Open [Issues](../../issues) for bugs/ideas.
* Check [CONTRIBUTING.md](CONTRIBUTING.md).

---

## ⚖️ Disclaimer

This project is purely for **educational and personal learning**.
All trademarks, names, and logos belong to their respective owners.

