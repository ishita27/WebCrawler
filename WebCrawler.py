import operator
from bs4 import BeautifulSoup
import requests
from collections import Counter

def start(url):
    wordlist=[]
    source = requests.get(url).text

    soup = BeautifulSoup(source,'html.parser')

    for each_text in soup.findAll('div',{'class':'entry-content'}):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        cleanlist(wordlist)

def cleanlist(wordlist):
    clean = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range (0,len(symbols)):
            word = word.replace(symbols[i],'')

        if len(word)>0:
            clean.append(word)
    create_dict(clean)

def create_dict(clean):
    word_count={}
    for word in clean:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    c = Counter(word_count)

    top = c.most_common(5)
    print(top)
    

if __name__== '__main__':
    start("https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/")
