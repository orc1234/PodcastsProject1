import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import warnings
import ast
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")
import time
time.sleep(3)
from sklearn.preprocessing import LabelEncoder







podcasts_df = pd.read_csv('copy_df_podcasts.csv', header=0, sep=',')
podcasts_df=podcasts_df.drop(["link"], axis=1)
podcasts_df.set_index('podcast_name', inplace=True)
columnsToEncode = list(podcasts_df.select_dtypes(include=['category', 'object']))
le = LabelEncoder()
for feature in columnsToEncode:
    try:
        podcasts_df[feature] = le.fit_transform(podcasts_df[feature])
    except:
        print('Error encoding ' + feature)
'''
cat_vars=['link']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(podcasts_df[var], prefix=var)
    data1=podcasts_df.join(cat_list)
    podcasts_df=data1
cat_vars=['link']
data_vars=podcasts_df.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=podcasts_df[to_keep]
data_final.columns.values
print(podcasts_df)
'''

podcasts_df['ListenScore'] = podcasts_df['ListenScore'].mask(podcasts_df['ListenScore'] < 60, 0)
podcasts_df['ListenScore'] = podcasts_df['ListenScore'].mask(podcasts_df['ListenScore'] >=60, 1)



features = podcasts_df.columns[podcasts_df.columns != 'ListenScore']
X = podcasts_df[features]
y = pd.Series(podcasts_df['ListenScore'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf_model = LogisticRegression().fit(X_train, y_train)
y_pred = clf_model.predict(X_test)
resDF = pd.DataFrame({"Actual":y_test,"Predicted":y_pred})
resDF["correct"] = abs((resDF["Actual"] ^ resDF["Predicted"]) - 1)
resDF[resDF["correct"] == 1]
print(resDF)
print(accuracy_score(y_test, y_pred, normalize=False))
print(accuracy_score(y_test, y_pred, normalize=True))
resDF.to_csv('ML.csv')