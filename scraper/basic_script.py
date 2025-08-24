from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from io import StringIO

driver = webdriver.Chrome()
driver.get("https://www.espncricinfo.com/series/ipl-2025-1449924/kolkata-knight-riders-vs-royal-challengers-bengaluru-1st-match-1473438/full-scorecard")

# Wait for at least one table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "table"))
)

# Get HTML
html = driver.page_source

# Read tables
tables = pd.read_html(StringIO(html))

# Example: print first table (KKR Batting)
print("\nKKR Batting:\n", tables[0][1])

# Example: print second table (RCB Bowling)
print("\nRCB Bowling:\n", tables[1][1])

# Save each table separately
for i, table in enumerate(tables):
    table.to_csv(f"table_{i}.csv", index=False)

driver.quit()
