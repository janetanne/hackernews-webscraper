import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

all_stories = soup.find_all(class_='athing')
print(all_stories[0])

# for story in all_stories:
#     title = story.find(class_='storylink')
#     author = story.find(class_='score')
#     score = story.find(class_='hnuser')
#     print(title.text, author.text, score.text)

# title_results = soup.find_all('a', class_='storylink')
# first_title = title_results[0].text

# score_results = soup.find_all('span', class_='score')
# first_score = score_results[0].text

# author_results = soup.find_all('a', class_='hnuser')
# first_author = author_results[0].text

def get_titles(lst):
    """Parses titles from soup results."""

    for title in lst:
        story_title = title.text
        print(title)

# gather titles, corresponding author names, points values
# print as a list of objects
# check first & last to make sure it's aligned (first author / last author are aligned)
