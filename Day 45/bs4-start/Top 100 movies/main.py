from pickletools import StackObject

import requests
from bs4 import BeautifulSoup

best_movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(best_movies_url).text
soup = BeautifulSoup(response)

best_movies = soup.find_all(name="div", class_="article-title-description__text")

list = [movie.h3.getText() for movie in best_movies]
movie_title = list[::-1]
print(movie_title)

print(list)