
from locale import D_FMT
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def wordclouds(speech):
    wordcloud = WordCloud().generate(speech)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()