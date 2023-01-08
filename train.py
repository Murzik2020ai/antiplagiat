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
parser.add_argument("path", type=str,
                    help="folder with files to train model")
parser.add_argument("dir1", type=str,
                    help="folder for files1")
parser.add_argument("dir2", type=str,
                    help="folder with files2")
parser.add_argument("-m", "--model", action="count",
                    help="train model")
parser.add_argument("modelname", type=str,
                    help="name of file with trained model")


args = parser.parse_args()
PATH_TO_DATA = ""
dir = args.path
directory = PATH_TO_DATA+dir

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
df_train = pd.DataFrame(list(zip(lst_text,lst_names)),columns =['code','names'])
logger = logging.getLogger('logger_name')
logger.debug('debug info')
logger.info("dataframe created good.")
# regex for tokenizing
TOKEN_RE = re.compile(r'[\w\d]+')
MAX_DF = 0.8
MIN_COUNT = 5

df_train['keywords'] = df_train['code']
df_train['keywords'] = df_train['keywords'].apply(take_keywords)

vect = TfidfVectorizer(
    tokenizer=tokenize_text_simple_regex,
    max_df=MAX_DF,
    min_df=MIN_COUNT
)

# vectorize text with tfidf-vectoriser
logger.info("texts vectorised good.")
X_txt = vect.fit_transform(df_train['keywords'])

df_X_tr = pd.DataFrame(X_txt.toarray())
# init random forest classifier
clf = RandomForestClassifier(
    n_estimators=50,n_jobs=-1, random_state=RS
    )
# train classifier
clf.fit(df_X_tr,df_train['names'])
logger.info("dataframe created good.")
#clf.score(df_X_tr,df_train['names'])
#save our classifier to a file
modelfilename = args.modelname
pickle.dump(clf, open(modelfilename, 'wb'))
logger.info("model saved.")
