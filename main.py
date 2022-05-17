from data_cleaner import d_2019,d_2020,s_2019,s_2020
from wordclouds import wordclouds
if __name__ == '__main__':
    wordclouds(str(d_2020))
    wordclouds(str(d_2019))
    wordclouds(str(s_2020))
    wordclouds(str(s_2019))