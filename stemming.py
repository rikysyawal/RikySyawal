#import nltk package
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


# Memanggil nltk downloader
# nltk.download()
# True
porter = PorterStemmer()
sentence = input("Input sentence: ")
def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


x = stemSentence(sentence)


print("Senctence after tokenize and stemming: "+ x)












# from nltk.stem import LancasterStemmer

# #membuat object class PoreterStemmer

# porter = PorterStemmer()
# lencester = LancasterStemmer()

# #contoh kata yang akan distemmer

# print("Porter Stemmer")
# print(porter.stem("cats"))
# print(porter.stem("trouble"))
# print(porter.stem("troubled"))
# print(porter.stem("troubling"))

# print("Lancaster Stemmer")
# print(lencester.stem("cats"))
# print(lencester.stem("trouble"))
# print(lencester.stem("troubled"))
# print(lencester.stem("troubling"))



