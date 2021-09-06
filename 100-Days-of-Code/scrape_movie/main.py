from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://www.imdb.com/chart/top/?ref_=nv_mv_250")

movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

movie_tags = soup.select(".titleColumn a")

movie_list = [tag.getText() for tag in movie_tags]


with open(file="movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
