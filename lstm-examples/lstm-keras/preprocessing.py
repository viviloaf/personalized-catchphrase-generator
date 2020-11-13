import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer, ENGLISH_STOP_WORDS


'''
list of functions that

convert text data into integer representation

'''

def word_vectorizer(pd_series, stop_words=None, ngram_range=(1,1)):
    '''
    Processes a datatype of text: Series, DataFrame, List
    '''
    cv = CountVectorizer(stop_words=stop_words, ngram_range=ngram_range)
    matrix = cv.fit_transform(df_vivian_content)
    freqs = zip(cv.get_feature_names(), matrix.sum(axis=0).tolist()[0])
    df_words = pd.DataFrame(freqs, columns=['word','count'])
    df_words.sort_values(by='count', ascending=False).head(20)
    return cv, df_words, matrix