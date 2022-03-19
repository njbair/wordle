import json
from urllib.request import urlopen

def five_letter_words(word_list):
  for word in word_list:
    if len(word) == 5:
      yield word

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'
response = urlopen(url)
data = json.loads(response.read())

with open('five-letter-words.json', 'w', encoding='utf-8') as f:
  json.dump(list(five_letter_words(data)), f, indent=2)