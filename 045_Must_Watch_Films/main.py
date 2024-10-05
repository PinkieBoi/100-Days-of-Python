import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url=URL).text
soup = BeautifulSoup(res, "html.parser")
wm_article = soup.find("article", class_="article category--movies")
movie_rankings = [film.getText() for film in wm_article.find_all("h3", class_="title")][::-1]

with open("movies.txt", "a") as file:
    for movie in movie_rankings:
        file.write(f"{movie}\n")
