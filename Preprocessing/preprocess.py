import re
regex = re.compile("[A-Za-z]+")

def words_only(text, regex=regex):
    try:
        return " ".join(regex.findall(text))
    except:
        return ""

from nltk.corpus import stopwords
print(stopwords.words('english'))

mystopwords = stopwords.words('english') + ['&', 'w/', '0\"', 'or', '1/8\"', 'only', 'from', 'of',
                                            'not', '/', 'ln'] + ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                                                 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                                                 'o', 'p', 'q', 'r', 's', 't', 'u',
                                                                 'v', 'w', 'x', 'y', 'z']


def remove_stopwords(text, mystopwords=mystopwords):
    try:
        return " ".join([token for token in text.split() if not token in mystopwords])
    except:
        return ""
