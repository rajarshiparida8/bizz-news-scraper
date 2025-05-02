from GoogleNews import GoogleNews
import json
from datetime import datetime
import os

# 1. Initialize GoogleNews object (set period to 1 day)
googlenews = GoogleNews(period='1d')

# 2. Search for India Business News
googlenews.search('India Business News')

# 3. Get results (list of articles with title, link, date, etc.)
results = googlenews.results()

# 4. Add timestamp (so you know when the data was last updated)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 5. Prepare final data
data = {
    "timestamp": timestamp,
    "results": results
}

# Ensure the docs/ folder exists
os.makedirs("docs", exist_ok=True)

# Save in docs/news_output.json
with open("docs/news_output.json", "w") as f:
    json.dump(data, f, indent=4, default=str)  # Fix: handles datetime objects



print("✅ Scraping complete. Saved to news_output.json")
