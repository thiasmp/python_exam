from data_cleaner import data_clean_corpus
from fetch_speech_to_df import spoke_persons
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)

#Create subplots for each comedian
for index, speeches in enumerate(data_clean_corpus.columns):
    wc.generate(data_clean_corpus.speeches[speeches])
    
    plt.subplot(3, 4, index+1)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(spoke_persons[index])
    
plt.show()
#wordclouds(str(data_clean_corpus))               