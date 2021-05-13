import re
import string
import unicodedata

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')
PUNCTUATIONS = str.maketrans({key: None for key in string.punctuation+"¿¡?!"})


class Preprocess:

    def clean_dataset(self, dataset):
        for index, row in dataset.iterrows():
            clean_text = " "
            lower_text = row.text.lower()
            tweet_tokens = [
                word for word in lower