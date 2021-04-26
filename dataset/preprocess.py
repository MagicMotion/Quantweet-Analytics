import re
import string
import unicodedata

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')
PUNCTUATIONS = str.maketrans({key: None for key in string.punctuation+"¿¡?!"})


class Pr