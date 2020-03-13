import re
from joblib import dump, load
import pandas as pd
from collections import Counter

class classPredictor:

    def __init__(self, txt1=None, txt2=None, txt3=None, txt4=None, txt5=None) -> None:
        # self.model = False
        #
        # if txt1 is None:
        #     self.model = True
        # else:
        #     self.txts = [txt1, txt2, txt3, txt4, txt5]
        self.txts = [txt1, txt2, txt3, txt4, txt5]


        self.stopwords = self.loadStopWords()

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
    def loadStopWords(path='/Users/romakindmitriy/Desktop/hack_days/docs/stopwords.txt') -> list:
        with open(path, 'r') as f:
            stopwords = f.readlines()

        stopwords = list(map(lambda x: x[:-1], stopwords))
        return stopwords

    def preprocess(self, msg):
        msg_l = msg.lower()
        msg_words = self.words_only(msg_l)
        msg_clear = self.remove_stopwords(msg_words, self.stopwords)
        return msg_clear

    @staticmethod
    def __load_txt(txt):
        data = []

        with open(txt, 'r') as f:
            data = f.readlines()

        data = list(map(lambda x: x[:-1], data))
        text = " ".join(data)
        return text

    def __getMax(self, result):
        res = result.items()
        rmax = max(res, key=lambda x: x[1])
        rmin = min(res, key=lambda x: x[1])
        if rmax[1] > rmin[1]:
            return rmax[0]
        elif rmin[1] == rmax[1]:
            return 6

    @staticmethod
    def predictByModel(msg, path_to_model='/Users/romakindmitriy/PycharmProjects/DataScienceHackDays/model/ExtraTreesClassifier.joblib') -> int:
        clf = load(path_to_model)
        data = [[msg]]
        df = pd.DataFrame(data, columns=['message'])
        result = int(clf.predict(df['message'][:1])[0])
        return result

    def predictClass(self, msg) -> int:
        msg_clear = self.preprocess(msg)
        print(msg_clear)

        # if self.model is False:

        result = {}

        for i in range(len(self.txts)):

            text = self.__load_txt(self.txts[i])

            list_msg_clear = msg_clear.split(' ')

            local_result = []
            for word in list_msg_clear:
                regc = re.compile(fr"{word}")

                local_result.append(self.words_only(text, regc))

            local_result = [x for x in local_result if x != '']
            # print(local_result)

            result[i+1] = len(local_result)

        answ = self.__getMax(result)

        if answ == 6:
            answ = self.predictByModel(msg_clear)

        return answ

        # elif self.model is True:
        #     result = self.predictByModel(msg_clear)
        #     return result


if __name__ == '__main__':
    # clcr = classPredictor('./df1.txt', './df2.txt', './df3.txt', './df4.txt', './df5.txt')
    clcr = classPredictor()
    msg = 'STRAWBERRIES,FRZ,SWTND,SLICED'
    print(clcr.predictClass(msg))

# CEREALS RTE,QUAKER,SHREDDED WHEAT,BAGGED CRL