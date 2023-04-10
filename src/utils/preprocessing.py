import re
import string
from typing import Optional

import nltk
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)


def to_lower(text: str) -> str:
    return text.lower()


def remove_html_tag(text: str) -> str:
    return re.sub(re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'), '', text)


def remove_url(text: str) -> str:
    return re.sub(r'https?://\S+|www\.\S+', '', text)


def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_number(text: str) -> str:
    return re.sub('\d+', '', text)


def remove_stopword(text: str, stop_words: Optional[set] = None) -> str:
    if stop_words is None:
        stop_words = set(stopwords.words('english'))

    return ' '.join([token for token in word_tokenize(text) if token not in stop_words])


def remove_n_chars(text: str, n=2) -> str:
    return ' '.join([w for w in text.split(' ') if len(w) > n])


def tag_pos(text: str) -> str:
    result = []
    tags = pos_tag(word_tokenize(text))

    pos_dict = {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'N': wordnet.NOUN,
        'R': wordnet.ADV
    }

    for word, tag in tags:
        result.append(tuple([word, pos_dict.get(tag[0])]))

    return result


def lemmatize_word(text: str) -> str:
    lemmas = []
    lemmatizer = WordNetLemmatizer()
    pos_words = tag_pos(text)

    for word, tag in pos_words:
        if tag is None:
            lemmas.append(word)
        else:
            lemmas.append(lemmatizer.lemmatize(word, tag))

    return " ".join(lemmas)
