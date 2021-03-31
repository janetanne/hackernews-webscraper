# Exercise: 
# Create a web scraper that scrapes Hacker News and gathers the titles, corresponding author names, point values.
# Print it as a list of objects.
# Tip: Check first & last to make sure it's aligned (first author / last author are aligned)

import requests
from bs4 import BeautifulSoup

# Using BeautifulSoup to scrape the webpage:
URL = "https://news.ycombinator.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# data for each attribute; pulled at the same time as the page is live
titles_soup = soup.find_all(class_='athing')
# subtext soup contains the info for author & votes, so will iterate over that data separately
subtext_soup = soup.find_all(class_='subtext')

# I created a class for "Story". This is probably overkill, but it stores data nicely, and I was asked for a list of objects :)
class Story:
    """
    A class to represent a story. 
    Has attributes: title, author, and points.
    """
    
    def __init__(self, title, author, score):
        self.title = title
        self.author = author
        self.score = score
    
    def __repr__(self):
        return(f'{self.__class__.__name__}('
        f'{self.title!r}, {self.author!r}, {self.score!r})')

def create_titles_list(lst):
    """Given a list of Hacker News data, returns the title of each top story."""

    title_list = []

    for item in lst:
        title = item.find(class_='storylink')
        title_list.append(title.text)
    
    return title_list

def create_authors_list(lst):
    """Given a list of Hacker News data, returns the author of each top story."""

    authors_list = []

    for item in lst:
        author = item.find(class_='hnuser')
        if author is None:
            authors_list.append("N/A")
        else:
            authors_list.append(author.text)
    
    return authors_list

def create_scores_list(lst):
    """Given a list of Hacker News data, returns the points of each top story."""

    scores_list = []

    for item in lst:
        score = item.find('span', class_='score')
        if score is None:
            scores_list.append("N/A")
        else:
            scores_list.append(score.text)
    
    return scores_list

top_titles = create_titles_list(titles_soup)
top_authors = create_authors_list(subtext_soup)
top_scores = create_scores_list(subtext_soup)

all_stories = [] 

for i in range(len(top_titles)):
    _story = Story(title=top_titles[i], 
                   author=top_authors[i], 
                   score=top_scores[i])
    all_stories.append(_story)

print(all_stories)