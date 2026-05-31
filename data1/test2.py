from firecrawl import FirecrawlApp
import json

app = FirecrawlApp(api_key="fc-33d34594ec284605b4529c9409937ab5")

result = app.scrape_url("https://cvr.ac.in/home4/")

with open("cvr_college.txt", "w", encoding="utf-8") as f:
    f.write(result.markdown)

print("Saved successfully")