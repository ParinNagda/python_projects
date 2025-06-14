from cgitb import reset

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
text = soup.find_all(name="span", class_="titleline")
articleTexts = []
articleLinks = []

for val in text:
    articleText = val.a.getText()
    articleTexts.append(articleText)
    articleLink = val.a.get("href")
    articleLinks.append(articleLink)

articleUpvotes = [score.getText().split(" ")[0] for score in soup.find_all(name="span", class_="score")]

print(articleTexts)
print(articleLinks)
print(articleUpvotes)