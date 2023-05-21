import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from functools import partial
from sklearn.feature_extraction.text import CountVectorizer

tokenizer = RegexpTokenizer(r'\w+')

nltk.download('stopwords')
stop_word = stopwords.words('english')
stopword_set = set(stopwords.words('english'))  

def to_lower(review):
    return review.lower()

def is_stopword(word, stop_words):
    return word not in stop_words

def filter_stopwords(review, stop_words):
    return list(filter(partial(is_stopword, stop_words = stop_words), review))


def tokenization(doc_squeeze):
    #reviews = df['text'].squeeze()
    doc_squeeze = doc_squeeze.map(to_lower)
    doc_squeeze = doc_squeeze.map(tokenizer.tokenize)
    doc_squeeze = doc_squeeze.map(partial(filter_stopwords, stop_words = stopword_set))
    doc_squeeze_str = [' '.join(rev) for rev in doc_squeeze]
    return doc_squeeze_str
        


def more_relevant_words(corpus, n=1, k=1):
    vec = CountVectorizer(ngram_range=(k, k), 
                          stop_words= stop_word)
    bag_of_words = vec.fit_transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    
    words_freq = [(word, sum_words[0, idx]) 
                  for word, idx in vec.vocabulary_.items()]
    
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]
