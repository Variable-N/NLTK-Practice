from tkinter import W
import nltk  
from nltk.tokenize import word_tokenize

s = "Hello! This is a test. Mr. O'Neill said reaction to Sea Container's proposal “hasn't been very positive.” In New York Stock Exchange composite trading yesterday, Sea Containers closed at $62.625, down 62.5 cents."

# Tokenizing sentences into words using word_tokenize
print("\n Tokenizing sentences into words using word_tokenize \n")
tokens = word_tokenize(s)
print(tokens)
print(type(tokens))

# Tokenizing sentences into words using treebank tokenizers
print("\n Tokenizing sentences into words using treebank tokenizers \n")

from nltk.tokenize import TreebankWordTokenizer

x = TreebankWordTokenizer()
tree_bank_tokenizers = x.tokenize(s)

print(tree_bank_tokenizers)

# WordPunktTokenizer Class    
print("\n WordPunktTokenizer Class \n")
from nltk.tokenize import WordPunctTokenizer

x = WordPunctTokenizer()
word_punct_tokenizer = x.tokenize(s)

print(word_punct_tokenizer)

# Tokenizing text into sentences
print("\n Tokenizing text into sentences \n")
from nltk.tokenize import sent_tokenize

x = sent_tokenize(s)
print(x)

# Sentence tokenization using regular expressions
print("\n Sentence tokenization using regular expressions \n")
import nltk
from nltk.tokenize import RegexpTokenizer 

tokenizer = RegexpTokenizer("[\w']+")
x = tokenizer.tokenize(s)
print(x)

