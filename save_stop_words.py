import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))


with open('docs/freq_words.txt', 'r') as f:
    words = f.readlines()

with open('docs/translate_freq_words.txt', 'r') as f:
    translate_words = f.readlines()

translate_words = list(map(lambda x: x.lower(), translate_words))
concat_words = list(zip(words, translate_words))

# print(concat_words)
print(len(concat_words))

# with open('stopwords.txt', 'w') as f:
#     for word in concat_words:
#         if word[0] == word[1]:
#             pass
#             # f.write(word[0])
#         else:
#             print(word)

filtered_words = []
for word in concat_words:
        if word[0] != word[1]:
            filtered_words.append(word)

ready_words = []
for word in filtered_words:
    tokenized = sent_tokenize(word[0])
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        # print(tagged)

        for w in tagged:
            if w[1] == 'NN' or w[1] == 'NNS':
                ready_words.append(w[0])


# print(*ready_words, sep='\n')

ready_words = list(set(ready_words))

print(len(ready_words))

# 4235
# 2525