# Contributing to Cricinfo Scorecard Scraper 🏏

Thanks for checking out this project! This scraper is built for **educational purposes only** and is still evolving. Contributions of all shapes and sizes are welcome — bug fixes, docs, new ideas, or even reporting what didn’t work.

---

## 🏃 Getting Started

1. **Fork the repo** and clone your fork:

   ```bash
   git clone https://github.com/khushal-coder-learner/espncricinfo-scorecard-scraper.git
   cd espncricinfo-scorecard-scraper
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\Activate.ps1  # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run a test scrape**:

   ```bash
   python -m scraper.main
   ```

Outputs will appear under `data/`.

---

## 🚀 How to Contribute

* **Bug Fixes** → Example: parsing fails for Super Overs, missing bowling or fall of wickets and messy formatting.
* **Features** → Example: CSV/Excel export, caching, retries, or better logging.
* **Docs** → Improve README, add examples, or explain tricky selectors.
* **Examples** → Add JSON outputs from more matches so others can see edge cases.

---

## 📌 Workflow

1. Create a branch for your change:

   ```bash
   git checkout -b fix/fow-parsing
   ```
2. Make your changes and test them.

3. Commit with a clear message (try `feat:`, `fix:`, or `docs:`):

   ```bash
   git commit -m "fix: handle NaN in Super Over totals"
   ```
4. Push your branch and open a Pull Request. 🎉

---

## 🔍 Reporting Issues

If you hit a bug, please [open an issue](../../issues/new) and include:

* The URL you tried.
* What you expected vs what you got.
* Any console errors or JSON output.

---

## 📋 Code Style

* Follow Python best practices (PEP8-ish).
* Keep functions **short and focused**.
* If you add logic, also add a **unit test** (even a tiny one).
* Use meaningful variable names (no `x`, `y` for players 😉).

---

## 💡 Tips for First-Time Contributors

* Check the [good first issue](../../labels/good%20first%20issue) label.
* Don’t be afraid to ask questions in [Discussions](../../discussions).
* Even small fixes (like improving logging) are valuable.

---

## ❤️ Code of Conduct

Be kind, respectful, and assume good intent. Disagree with ideas, not people.

---
