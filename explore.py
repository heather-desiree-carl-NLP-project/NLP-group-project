import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# for colormap tools
from matplotlib import cm
import pandas as pd
import nltk
import unicodedata
import re
import seaborn as sns
from wordcloud import WordCloud


def get_word_counts_series(df, column):
    '''
    This function takes in a dataframe
    and the column you want to create the word counts of
    returns a series of the words and their counts
    You can get the top 20 or whatever from that later
    '''
    words = ' '.join(df[column])
    
    words_list = words.split()
    
    word_counts = pd.Series(words_list).value_counts()
    
    return word_counts


def plot_overlap_stacked_bar(word_counts, category, num_top = 20, colors = None):
    '''
    This function takes in word_counts df
        - Must have counts for each category as well as a category named 'all'
    category you want to sort by (aka top 20 words in java readmes)
    num_top is how many words you want to see the proportion of, default = 20
    Default colors are tab10 but you can customize that
    
    '''
    plt.figure(figsize=(16, 9))
    plt.rc('font', size=16)
    # axis=1 in .apply means row by row
    (word_counts.sort_values(by='all', ascending=False)
     .head(num_top)
     .apply(lambda row: row / row['all'], axis=1)
     .drop(columns='all')
     .sort_values(by=category)
     .plot.barh(stacked=True, width=1, ec='grey', color = colors))
    plt.legend(bbox_to_anchor= (1.03,1))
    plt.title(f'% of most common {num_top} {category} Readme Words\n')
    plt.xlabel('\nProportion of Overlap')
    # make tick lables display as percentages!! 
    plt.gca().xaxis.set_major_formatter(mpl.ticker.FuncFormatter('{:.0%}'.format))
    
    plt.show()