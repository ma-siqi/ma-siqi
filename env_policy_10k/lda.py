import json
import tomotopy as tp
import string
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import sys

year = str(sys.argv[1])
quarter = str(sys.argv[2])
quarter_str = 'QTR' + quarter

path_name = year + "q" + quarter + "ls"


mdl = tp.LDAModel(k=20)
input_path = f'lda/rev{year}q{quarter}.json'
#input_path = "lists/climate_lda/2016/rev2016q1.json"
punctuations = list(string.punctuation)
stop_words = set(stopwords.words('english'))
word_list = ["item", "i", "''", "``", "'s" "’", "n't", "►", "...", "’", "'s", "video", 
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
             'environment','environmental','climate','sustainability','sustainable','may','could','would','should',
             '2016', '2017','2018', '2019', '2020', '2021','May','March','June', 'Jan', '30', '31','September', 'December',
             'Dec', 'Nov','Sept']

def preprocess(line):
    tokens = word_tokenize(line)
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if word not in punctuations]
    tokens = [word for word in tokens if word not in word_list]
    return (" ").join(tokens)

with open(input_path, "r") as f:
    data = json.load(f)
    for d in data:
        for lines in data[d]["Rev_Text"]:
            lines = preprocess(lines)
            mdl.add_doc(lines.strip().split())

print("Training model...")
for i in range(0, 100, 10):
    mdl.train(10)
    print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))

for k in range(mdl.k):
    print('Ttop 10 words of topic #{}'.format(k))
    print(mdl.get_topic_words(k, top_n=10))

print("Summary wildfire..")


mdl.summary()


sys.stdout = open(f"lda{year}q{quarter}.txt", "w")


mdl.summary()


sys.stdout.close()


