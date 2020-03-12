import re
from nltk.corpus import stopwords

class classCreator:

    # def __init__(self, txt1, txt2, txt3, txt4, txt5, path_stopwords='./../stopwords.txt') -> None:
    def __init__(self, path_stopwords='./../stopwords.txt') -> None:

        # self.txt1 = txt1
        # self.txt2 = txt2
        # self.txt3 = txt3
        # self.txt4 = txt4
        # self.txt5 = txt5

        # self.txts = [txt1, txt2, txt3, txt4, txt5]

        self.stopwords = self.loadStopWords()
        # print(self.stopwords[:10])
        # print('crl' in self.stopwords)
        # print(len(self.stopwords))

        super().__init__()

    @staticmethod
    def remove_stopwords(text, mystopwords):
        try:
            return " ".join([token for token in text.split() if not token in mystopwords])
        except:
            return ""

    @staticmethod
    def words_only(text, regex=re.compile("[A-Za-z]+")):
        try:
            return " ".join(regex.findall(text))
        except:
            return ""

    @staticmethod
    def loadStopWords(path='/Users/romakindmitriy/Desktop/hack_days/stopwords.txt') -> list:
        with open(path, 'r') as f:
            stopwords = f.readlines()

        stopwords = list(map(lambda x: x[:-1], stopwords))
        return stopwords

    def preprocess(self, msg):
        msg_l = msg.lower()
        msg_words = self.words_only(msg_l)
        msg_clear = self.remove_stopwords(msg_words, self.stopwords)
        return msg_clear

    def predictClass(self, msg) -> int:
        msg_clear = self.preprocess(msg)
        print(msg_clear)
        exit(0)

        result = []

        for txt in self.txts:

            data = []

            with open(txt, 'r') as f:
                data = f.readlines()

            text = " ".join(data)


if __name__ == '__main__':
    clcr = classCreator()
    msg = 'CEREALS RTE,QUAKER,SHREDDED WHEAT,BAGGED CRL'
    print(clcr.preprocess(msg))

# CEREALS RTE,QUAKER,SHREDDED WHEAT,BAGGED CRL