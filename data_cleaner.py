from locale import D_FMT
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from fetch_speech_to_df import data_df
import nltk
import re
import string
from sklearn.feature_extraction.text import CountVectorizer

#Words we found useless through most_common_words.py
lst_of_words_to_remove = ['kan','så','ved','dag','hele','igen','gør',
'ligger','kom','må','se','ser','går','tager','tage','tror','vi','er','et', 'måtte', 'måttet']
#set(stopwords.words('danish'))
stopwords = nltk.corpus.stopwords.words('danish')
for w in lst_of_words_to_remove:
    stopwords.append(w)


#function to clean speeches of a variety of punctuation, symbols, next lines etc.
def data_cleaner(text):  
    text = text.lower()
    #text = [w for w in text if not w in stopwords]

    text = re.sub('\[.*?\]', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(r'(?<=[.,])(?=[^\s])', r' ', text)
    
    return text

cleaned = lambda x: data_cleaner(x)

data_clean_corpus = pd.DataFrame(data_df.speeches.apply(cleaned))

#function to remove stopwords from speeches
def remove_stopwords():

    data_clean_corpus['speeches'] = data_clean_corpus['speeches'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))

    return data_clean_corpus

stopwords_corpus = remove_stopwords()


#function to create our document-term matrix.
def corpus_to_dtm():
    cv = CountVectorizer(stop_words=stopwords)
    data_cv = cv.fit_transform(data_clean_corpus.speeches)
    data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
    data_dtm.index = data_clean_corpus.index
    return data_dtm
