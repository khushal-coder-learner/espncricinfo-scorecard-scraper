Contributing to Cricinfo Scorecard Scraper 🏏

Thanks for checking out this project! This scraper is built for educational purposes only and is still evolving. Contributions of all shapes and sizes are welcome — bug fixes, docs, new ideas, or even reporting what didn’t work.

🏃 Getting Started

Fork the repo and clone your fork:

git clone https://github.com/<your-username>/cricscraper.git
cd cricscraper


Set up a virtual environment:

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\Activate.ps1  # Windows


Install dependencies:

pip install -r requirements.txt


Run a test scrape:

python -m cricscraper --url <scorecard-url>


Outputs will appear under data/.

🚀 How to Contribute

Bug Fixes → Example: parsing fails for Super Overs, or player roles leak into match_info.

Features → Example: CSV/Excel export, caching, retries, or better logging.

Docs → Improve README, add examples, or explain tricky selectors.

Examples → Add JSON outputs from more matches so others can see edge cases.

📌 Workflow

Create a branch for your change:

git checkout -b fix/fow-parsing


Make your changes and test them.

Run basic checks:

pytest -q


Commit with a clear message (try feat:, fix:, or docs:):

git commit -m "fix: handle NaN in Super Over totals"


Push your branch and open a Pull Request. 🎉

🔍 Reporting Issues

If you hit a bug, please open an issue
 and include:

The URL you tried.

What you expected vs what you got.

Any console errors or JSON output.

📋 Code Style

Follow Python best practices (PEP8-ish).

Keep functions short and focused.

If you add logic, also add a unit test (even a tiny one).

Use meaningful variable names (no x, y for players 😉).

💡 Tips for First-Time Contributors

Check the good first issue
 label.

Don’t be afraid to ask questions in Discussions
.

Even small fixes (like improving logging) are valuable.

❤️ Code of Conduct

Be kind, respectful, and assume good intent. Disagree with ideas, not people.