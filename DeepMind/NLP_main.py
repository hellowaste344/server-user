import nltk
nltk.download('punkt_tab')

# tokenizers
from nltk.tokenize import sent_tokenize
text = "Hello everyone. Welcome to My Darkness"
print(sent_tokenize(text))

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
print(tokenizer.tokenize(text))

from nltk.tokenize import word_tokenize
text = "hello everyone. Welcome to My Darkness"
print(word_tokenize(text))

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(text))

from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize("Let's see how it's working"))