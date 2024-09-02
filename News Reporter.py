import requests
import json
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-02&sortBy=publishedAt&apiKey=487fdc3a817b47629264ee425ffbab0b"
r = requests.get(url)
# print(r.text)
# json.loads(r.text)
news = json.loads(r.text)
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")