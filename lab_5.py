import pandas as pd   #Датасет из файла
import matplotlib.pyplot as plt    #Библиотека для построения графиков
import numpy as np    #Мат. функции и работа с массивами

from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics
    
#Чтение данных с файла с помощью pandas, создание датасета
data = pd.read_csv(r"C:\Users\Nova\Desktop\metrologia\weatherHistory.csv")

X=data['Temperature (C)']
Y=data['Apparent Temperature (C)']

print(X)



#print(list(data.columns))








# creating one hot encoding of the categorical columns.
#df = pd.get_dummies(data, columns =['Temperature (C)', 'Apparent Temperature (C)', 'Humidity',
                                    #'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)'])



#LogR = LogisticRegression (random_state = 0).fit(data['Temperature (C)'],data['Apparent Temperature (C)'])



#Эталонные метки
y_true = ["positive","negative","negative","positive","positive","positive","negative"]
          
#Предсказанные метки
y_pred = ["positive","negative","positive","positive","negative","positive","positive"]
P=0      
R=[]

R = sklearn.metrics.confusion_matrix(y_true, y_pred)
#R.dtype(int)

#LogR.score(X_test, Y_test)

print(type(P))
print(type(R))
#P = str(R[0][0]) + str(R[0][1])
#N = r[1][0] + r[1][1]


#print(N)