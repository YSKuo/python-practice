from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

info_list = []

article_tags = soup.select("a.storylink")
article_texts = []
article_links = []

for tag in article_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))


article_upvotes = [int(tag.getText().split()[0])
                   for tag in soup.select("span.score")]

max_votes = max(article_upvotes)
max_index = article_upvotes.index(max_votes)

print(article_texts[max_index], article_links[max_index])
# import lxml

# with open(file="website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.prettify())

# all_a_tags = soup.find_all(name="a")

# # for tag in all_a_tags:
# # print(tag.getText())
# # print(tag.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading)


# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())


# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
