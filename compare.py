import os
import numpy as np


import pandas as pd
import argparse
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import logging


from take_keywords import take_keywords
from tokenize_text_simple_regex import tokenize_text_simple_regex

RS = 42  # constant to fix random state


parser = argparse.ArgumentParser()
parser.add_argument("inputfile", type=str,
                    help="file with files to score")
parser.add_argument("scorefile", type=str,
                    help="file to store results of work")
parser.add_argument("-m", "--model", action="count",
                    help="use model")
parser.add_argument("modelname", type=str,
                    help="name of file with trained model")


args = parser.parse_args()

PATH_TO_DATA = ""
dir1 = "plagiat1"
directory = PATH_TO_DATA+dir1

# iterate over files in that directory
lst_names = []  #list for names of files
lst_text = []   #list for code from files
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        lst_names.append(f[6:])
        buff = ""  #we add all lines in one string
        with open(f) as file:
            lines = file.readlines()
            for line in lines:
                buff += line
            lst_text.append(buff)
            

#make dataframe
df = pd.DataFrame(list(zip(lst_text,lst_names)),columns =['code','names'])

logger = logging.getLogger('logger_name')
logger.debug('debug info')
logger.info("dataframe created good.")
# regex for tokenizing
TOKEN_RE = re.compile(r'[\w\d]+')
MAX_DF = 0.8
MIN_COUNT = 5


df['keywords'] = df['code']
df['keywords'] = df['keywords'].apply(take_keywords)

vect = TfidfVectorizer(
    tokenizer=tokenize_text_simple_regex,
    max_df=MAX_DF,
    min_df=MIN_COUNT
)

# vectorize text with tfidf-vectoriser
logger.info("texts vectorised good.")
X_txt = vect.fit_transform(df['keywords'])

df_X_tr = pd.DataFrame(X_txt.toarray())
modelfilename = args.modelname
clf = pickle.load(open(modelfilename, 'rb'))

pred = clf.predict_proba(df_X_tr)
pred = np.max(pred,axis=1)
df['labels'] = clf.predict(df_X_tr)
df['proba'] = pred
#df.to_csv('test02.csv',header=True,index=False)
#save probabilities to a file
df['proba'].to_csv(args.scorefile,header=False,index=False)

