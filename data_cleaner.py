from locale import D_FMT
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

stopwords = set(stopwords.words('danish'))

def data_cleaner(speech):
    with open(speech) as file:
        data = file.read()
        token = word_tokenize(data)
        token = list(map(str.lower, token))
        r_stopwords = [s for s in token if not s in stopwords]
        
        return r_stopwords
        #wordcloud = WordCloud().generate(data)

d_2020 = data_cleaner("d_tale_2020.csv")
d_2019 = data_cleaner("d_tale_2019.csv")
s_2020 = data_cleaner("s_tale_2020.csv")
s_2019 = data_cleaner("s_tale_2019.csv")

