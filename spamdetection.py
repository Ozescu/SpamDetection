"""
IDE : Google Colab 

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('spam.csv' , encoding='latin-1')

df

df['v1'] = df['v1'].map({'ham':0 , 'spam':1})

df.columns=['label' , 'message' , 'message1' , 'message2' , 'message3']

df.drop(columns=['message1' , 'message2' , 'message3'] , inplace= True)

df

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df['message'])
y = df['label']
x.shape , y.shape

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.2 , random_state=42)

model = MultinomialNB()
model.fit(x_train , y_train)

y_pred = model.predict(x_test)

accuracy = model.score(x_test , y_test)
print(accuracy)

