import librosa
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from librosa.feature import mfcc
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import pickle

filename = 'people.sav'
model1 = pickle.load(open(filename, 'rb'))

y11, sr11 = librosa.load('recorded.wav')
mfcch11 = librosa.feature.mfcc(y=y11, sr=sr11, n_mfcc=40)

a = model1.predict([mfcch11[0, :60]])
print(a)