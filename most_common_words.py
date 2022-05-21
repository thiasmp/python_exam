import pandas as pd
from collections import Counter
from data_cleaner import corpus_to_dtm, data_clean_corpus


data = corpus_to_dtm()
data = data.transpose()

def top_30_words():
    top_dict = {}
    for s in data.columns:
        top = data[s].sort_values(ascending=False).head(30)
        top_dict[s]= list(zip(top.index, top.values))
    #print(top_dict)
    return top_dict
top_dict = top_30_words()


def pull_top_words(top_dict):
    words = []
    for speeches in data.columns:
        top = [word for (word, count) in top_dict[speeches]]
        for t in top:
            words.append(t)
    word_counter = Counter(words).most_common        
    #print(word_counter)
pull_top_words(top_dict)    

#Hardcoded list of overused stopwords not contained in original stopwords list
#This list has been moved into data_cleaner hardcoded to stop circular dependency
lst_of_words_to_remove = ['kan','så','ved','dag','hele','igen','gør',
'ligger','kom','må','se','ser','går','tager','tage','tror','vi','er','et']