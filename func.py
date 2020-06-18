import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter

def url_from_file():
    with open(sys.argv[1], 'r') as f:
        urls = [line.rstrip('\n') for line in f]
    return urls

def text_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text


def top_words(text, number_of_words):
    words = text.lower().split()
    top = Counter(words).most_common(number_of_words)
    print("Чаще всего встречаются слова:", top)
