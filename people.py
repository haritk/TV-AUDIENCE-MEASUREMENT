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

y1, sr1 = librosa.load('new/1.wav')
y2, sr2 = librosa.load('new/2.wav')
y3, sr3 = librosa.load('new/3.wav')
y4, sr4 = librosa.load('new/4.wav')
y5, sr5 = librosa.load('new/5.wav')
y6, sr6 = librosa.load('new/6.wav')
y7, sr7 = librosa.load('new/7.wav')
y8, sr8 = librosa.load('new/8.wav')
y9, sr9 = librosa.load('new/9.wav')
y10, sr10 = librosa.load('new/10.wav')
#y11, sr11 = librosa.load('new/11.wav')
#y12, sr12 = librosa.load('new/12.wav')


mfccm1 = librosa.feature.mfcc(y=y1, sr=sr1, n_mfcc=40)
mfccm2 = librosa.feature.mfcc(y=y2, sr=sr2, n_mfcc=40)
mfccm3 = librosa.feature.mfcc(y=y3, sr=sr3, n_mfcc=40)
mfccm4 = librosa.feature.mfcc(y=y4, sr=sr4, n_mfcc=40)
mfccm5 = librosa.feature.mfcc(y=y5, sr=sr5, n_mfcc=40)
mfccm6 = librosa.feature.mfcc(y=y6, sr=sr6, n_mfcc=40)
mfccm7 = librosa.feature.mfcc(y=y7, sr=sr7, n_mfcc=40)
mfccm8 = librosa.feature.mfcc(y=y8, sr=sr8, n_mfcc=40)
mfccm9 = librosa.feature.mfcc(y=y9, sr=sr9, n_mfcc=40)
mfccm10 = librosa.feature.mfcc(y=y10, sr=sr10, n_mfcc=40)


y1, sr1 = librosa.load('p/r1.wav')
y2, sr2 = librosa.load('p/r2.wav')
y3, sr3 = librosa.load('p/r3.wav')
y4, sr4 = librosa.load('p/r4.wav')
y5, sr5 = librosa.load('p/r5.wav')
y6, sr6 = librosa.load('p/r6.wav')
y7, sr7 = librosa.load('p/r7.wav')
y8, sr8 = librosa.load('p/r8.wav')
y9, sr9 = librosa.load('p/r9.wav')
y10, sr10 = librosa.load('p/r10.wav')

mfccr1 = librosa.feature.mfcc(y=y1, sr=sr1, n_mfcc=40)
mfccr2 = librosa.feature.mfcc(y=y2, sr=sr2, n_mfcc=40)
mfccr3 = librosa.feature.mfcc(y=y3, sr=sr3, n_mfcc=40)
mfccr4 = librosa.feature.mfcc(y=y4, sr=sr4, n_mfcc=40)
mfccr5 = librosa.feature.mfcc(y=y5, sr=sr5, n_mfcc=40)
mfccr6 = librosa.feature.mfcc(y=y6, sr=sr6, n_mfcc=40)
mfccr7 = librosa.feature.mfcc(y=y7, sr=sr7, n_mfcc=40)
mfccr8 = librosa.feature.mfcc(y=y8, sr=sr8, n_mfcc=40)
mfccr9 = librosa.feature.mfcc(y=y9, sr=sr9, n_mfcc=40)
mfccr10 = librosa.feature.mfcc(y=y10, sr=sr10, n_mfcc=40)


y1, sr1 = librosa.load('new/h1.wav')
y2, sr2 = librosa.load('new/h2.wav')
y3, sr3 = librosa.load('new/h3.wav')
y4, sr4 = librosa.load('new/h4.wav')
y5, sr5 = librosa.load('new/h5.wav')
y6, sr6 = librosa.load('new/h6.wav')
y7, sr7 = librosa.load('new/h6.wav')
y8, sr8 = librosa.load('new/h8.wav')
y9, sr9 = librosa.load('new/h9.wav')
y10, sr10 = librosa.load('new/h10.wav')
#y11, sr11 = librosa.load('new/h11.wav')
#y12, sr12 = librosa.load('new/h12.wav')

mfcch1 = librosa.feature.mfcc(y=y1, sr=sr1, n_mfcc=40)
mfcch2 = librosa.feature.mfcc(y=y2, sr=sr2, n_mfcc=40)
mfcch3 = librosa.feature.mfcc(y=y3, sr=sr3, n_mfcc=40)
mfcch4 = librosa.feature.mfcc(y=y4, sr=sr4, n_mfcc=40)
mfcch5 = librosa.feature.mfcc(y=y5, sr=sr5, n_mfcc=40)
mfcch6 = librosa.feature.mfcc(y=y6, sr=sr6, n_mfcc=40)
mfcch7 = librosa.feature.mfcc(y=y7, sr=sr7, n_mfcc=40)
mfcch8 = librosa.feature.mfcc(y=y8, sr=sr8, n_mfcc=40)
mfcch9 = librosa.feature.mfcc(y=y9, sr=sr9, n_mfcc=40)
mfcch10 = librosa.feature.mfcc(y=y10, sr=sr10, n_mfcc=40)



#X = [mfccm1[0, :60], mfccm2[0, :60], mfccm3[0, :60], mfccm4[0, :60], mfccm5[0, :60], mfccm6[0, :60], mfccm7[0, :60], mfccm6[0, :60], mfccm9[0, :60], mfccm10[0, :60],mfccr1[0, :60], mfccr2[0, :60], mfccr3[0, :60], mfccr4[0, :60], mfccr5[0, :60], mfccr6[0, :60], mfccr7[0, :60], mfccr6[0, :60], mfccr9[0, :60], mfccr10[0, :60],mfcch1[0, :60], mfcch2[0, :60], mfcch3[0, :60], mfcch4[0, :60], mfcch5[0, :60], mfcch6[0, :60], mfcch7[0, :60], mfcch6[0, :60], mfcch9[0, :60], mfcch10[0, :60] ]
X = [mfccm1[0, :60], mfccm2[0, :60], mfccm3[0, :60], mfccm4[0, :60], mfccm5[0, :60], mfccm6[0, :60], mfccm7[0, :60], mfccm8[0, :60], mfccm9[0, :60], mfccm10[0, :60],mfccr1[0, :60], mfccr2[0, :60], mfccr3[0, :60], mfccr4[0, :60], mfccr5[0, :60], mfccr6[0, :60], mfccr7[0, :60], mfccr8[0, :60], mfccr9[0, :60], mfccr10[0, :60],mfcch1[0, :60], mfcch2[0, :60], mfcch3[0, :60], mfcch4[0, :60], mfcch5[0, :60], mfcch6[0, :60], mfcch7[0, :60], mfcch8[0, :60], mfcch9[0, :60], mfcch10[0, :60]
]
X = np.array(X)
#X.shape
p = ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r','h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h']
#np.array(p).shape

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X,p)



#neigh = KNeighborsClassifier(n_neighbors=7)
#neigh.fit(X, p)

filename = 'people.sav'
pickle.dump(gnb, open(filename, 'wb'))
