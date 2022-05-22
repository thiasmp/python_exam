from data_cleaner import stopwords_corpus
from sentida import Sentida
import numpy as np
import matplotlib.pyplot as plt


total = []
mean = []

def add_sentiment_to_df():

   

    for s in range(4):
        sentiment_total = Sentida().sentida(stopwords_corpus.speeches[s], 
                    output = "total")
        total.append(sentiment_total)

        sentiment_mean = Sentida().sentida(stopwords_corpus.speeches[s], 
                    output = "mean")
        mean.append(sentiment_mean)
    
    stopwords_corpus['total'] = total
    stopwords_corpus['mean'] = mean

    return stopwords_corpus

add_sentiment_to_df()