import requests
import json
query=input("enter your choice ")
url="https://newsapi.org/v2/everything?q={cricket}tesla&from=2025-01-22&sortBy=publishedAt&apiKey=f2687bb3ba514ebdb8a3b90a60c91a43"
r=requests.get(url)
# print(r.text)
news=json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
print(".................................................................................................")