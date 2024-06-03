from summarizers.sumy_summarization import sumy_summarizer
from summarizers.nltk_summarization import nltk_summarizer
from summarizers.spacy_summarization import spacy_summarizer
from summarizers.t5_summarization import t5_summarizer

import spacy

nlp = spacy.load("en_core_web_sm")

def readingTime(mytext):
    total_words = len([token.text for token in nlp(mytext)])
    estimatedTime = total_words / 200.0
    return estimatedTime

def get_text(url):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    
    page = urlopen(url)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p:p.text, soup.find_all('p')))
    return fetched_text
