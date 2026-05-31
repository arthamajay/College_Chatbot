from firecrawl import FirecrawlApp

print("Starting...")

app = FirecrawlApp(api_key="fc-45e4fbde66204c15859fc9e9ebd7f8a4")

print("Crawling website...")

result = app.crawl_url(
    "https://cvr.ac.in/home4/",
    limit=1
)

print(type(result))
print(result)
print(dir(result))

# with open("cvr_college.txt", "w", encoding="utf-8") as f:
#     f.write(result.markdown)

# print("Saved successfully")