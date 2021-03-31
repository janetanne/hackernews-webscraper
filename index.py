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
scores_soup = soup.find_all('span', class_='score')
authors_soup = soup.find_all('a', class_='hnuser')

top_stories = []

def create_title_list(lst):

    title_list = []

    for item in lst:
        title = item.find(class_='storylink')
        title_list.append(title.text)
    
    return title_list

def create_authors_list(lst):

    authors_list = []

    for item in lst:
        author = item.find(class_='hnuser')
        authors_list.append(author.text)

def create_score_list(lst):

    scores_list = []

    for item in lst:
        score = item.find(class_='score')
        scores_list.append(score.text)
    
    return scores_list

# # I created a class for "Story". This is probably overkill, but it stores data nicely, and I was asked for a list of objects :)

# class Story:
#     """
#     A class to represent a story. 
#     Has attributes: title, author, and points.
#     """
    
#     def __init__(self, title, author=None, points=None):
#         self.title = title

