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

# data for each attribute
# i'm pulling this all at the same time because the data could change if i pulled these at separate times
titles_soup = soup.find_all(class_='athing')
authors_soup = soup.find_all(class_='hnuser')
scores_soup = soup.find_all(class_='score')

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
        authors_list.append(item.text)
    
    return authors_list

def create_scores_list(lst):
    """Given a list of Hacker News data, returns the points of each top story."""

    scores_list = []

    for item in lst:
        scores_list.append(item.text)
    
    return scores_list

top_titles = create_titles_list(titles_soup)
top_authors = create_authors_list(authors_soup)
top_scores = create_scores_list(scores_soup)

