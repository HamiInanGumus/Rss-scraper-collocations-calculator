# This program calculates the collocations in the tokenized entries/articles
# of an rss/atom feed after the url of the feed is provided by the user.
# It provides the output in numerical order of the entries/articles.
# The program uses rss_scraper_tokenizedtext_class and its method to scrape the feed
# and instantiate tokenized text.

import nltk, re, pprint
from rss_scraper_tokenizedtext_class import *

rss_tokenized_entries = RssTokenizedText.tokenize()
collocations_list = []

def collocations():
    for article in rss_tokenized_entries:
        print(rss_tokenized_entries.index(article)+1)
        text = nltk.Text(article)
        text1 = text.collocations()

collocations()
