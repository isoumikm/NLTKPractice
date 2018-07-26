# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:59:28 2018

@author: Soumik Mitra
"""
# Tokenize Text using Pure Python
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print(html)
# The printed output results contains a lot of HTML tags that needs to be cleaned
# To clean them we can use BeautifulSoup
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip = True)
print(text)

# Let's convert that text into tokens by splitting the text
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
print(tokens)

# Count Word Frequency
from bs4 import BeautifulSoup
import urllib.request
import nltk
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

# There are some words like The, Of, a, an. These are stopwords. Generally stop words should be removed
from nltk.corpus import stopwords
stopwords.words('english')
# cleaning the tokens
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
        
# Final Code
from bs4 import BeautifulSoup
 
import urllib.request
 
import nltk
 
from nltk.corpus import stopwords
 
response = urllib.request.urlopen('http://php.net/')
 
html = response.read()
 
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)
 
tokens = [t for t in text.split()]
 
clean_tokens = tokens[:]
 
sr = stopwords.words('english')
 
for token in tokens:
 
    if token in stopwords.words('english'):
 
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)
 
for key,val in freq.items():
 
    print (str(key) + ':' + str(val))
freq.plot(20,cumulative = False)

# Tokenize texr using NLTK Sentence Tokenizer
from nltk.tokenize import sent_tokenize
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))

from nltk.tokenize import sent_tokenize
 
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
 
print(sent_tokenize(mytext))

# Tokenize text using NLTK Word Tokenizer
from nltk.tokenize import word_tokenize
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(word_tokenize(mytext))

# The word Mr. is one word as expected
# NLTK uses PunktSentenceTokenizer which is a part of nltk.tokenize.punkt module

from nltk.tokenize import sent_tokenize
 
mytext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
 
print(sent_tokenize(mytext,"french"))

# WordNet
from nltk.corpus import wordnet
 
syn = wordnet.synsets("pain")
 
print(syn[0].definition())
 
print(syn[0].examples())

#####

from nltk.corpus import wordnet
 
syn = wordnet.synsets("NLP")
 
print(syn[0].definition())
 
syn = wordnet.synsets("Python")
 
print(syn[0].definition())

# Synonyms

from nltk.corpus import wordnet
 
synonyms = []
 
for syn in wordnet.synsets('Computer'):
 
    for lemma in syn.lemmas():
 
        synonyms.append(lemma.name())
 
print(synonyms)

# Antonyms
from nltk.corpus import wordnet
 
antonyms = []
 
for syn in wordnet.synsets("small"):
 
    for l in syn.lemmas():
 
        if l.antonyms():
 
            antonyms.append(l.antonyms()[0].name())
 
print(antonyms)

# NLTK Word Stemming- Porter Stemming Algo There is Lancaster Stemming algo too. The result differs
from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
 
print(stemmer.stem('working'))

# Stemming non-English words
from nltk.stem import SnowballStemmer
 
print(SnowballStemmer.languages)
########
from nltk.stem import SnowballStemmer
 
french_stemmer = SnowballStemmer('french')
 
print(french_stemmer.stem("French word"))

# Lemmatizing word using WordNet
from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
 
print(stemmer.stem('increases'))

# Lematize
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
 
print(lemmatizer.lemmatize('increases'))

# The result might end up with a synonym or a different word with the same meaning.

# Sometimes, if you try to lemmatize a word like the word playing, it will end up with the same word.

# This is because the default part of speech is nouns. To get verbs, you should specify it like this:

from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
 
print(lemmatizer.lemmatize('playing', pos="v"))

## 
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
 
print(lemmatizer.lemmatize('playing', pos="v"))
 
print(lemmatizer.lemmatize('playing', pos="n"))
 
print(lemmatizer.lemmatize('playing', pos="a"))
 
print(lemmatizer.lemmatize('playing', pos="r"))

# Stemming and Lemmatization Difference
from nltk.stem import WordNetLemmatizer
 
from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
 
lemmatizer = WordNetLemmatizer()
 
print(stemmer.stem('stones'))
 
print(stemmer.stem('speaking'))
 
print(stemmer.stem('bedroom'))
 
print(stemmer.stem('jokes'))
 
print(stemmer.stem('lisa'))
 
print(stemmer.stem('purple'))
 
print('----------------------')
 
print(lemmatizer.lemmatize('stones'))
 
print(lemmatizer.lemmatize('speaking'))
 
print(lemmatizer.lemmatize('bedroom'))
 
print(lemmatizer.lemmatize('jokes'))
 
print(lemmatizer.lemmatize('lisa'))
 
print(lemmatizer.lemmatize('purple'))

# Stemming works on words without knowing its context and that’s why stemming has lower accuracy and faster than lemmatization.

# In my opinion, lemmatizing is better than stemming. Word lemmatizing returns a real word even if it’s not the same word, it could be a synonym, but at least it’s a real word.

# Sometimes you don’t care about this level of accuracy and all you need is speed, in this case, stemming is better.