import codecs
from matplotlib import pyplot as plt
from matplotlib import mlab
import numpy as np
from pymystem3 import Mystem
import re
from sklearn import grid_search, svm
m = Mystem()

a = codecs.open('sonets.txt', 'r', 'utf-8')
text1 = a.read()
a.close()

b = codecs.open('anna.txt', 'r', 'utf-8')
text2 = b.read()
b.close()

corpus1 = re.split('[.!?]+', text1)
corpus2 = re.split('[.!?]+', text2)

vowels = ['а', 'я', 'ы', 'и', 'э', 'е', 'у', 'ю', 'о', 'ё']

print(corpus1[-1])

sonets = []
for c in corpus1:
    sent = []
    cc = re.sub('(,|:|;|\r\n|")', '', c.lower())
    sent.append(len(re.sub(' ', '', cc)) - 1)
    sent.append(len(''.join(set(re.sub(' ', '', cc)))) - 1)
    n = 0
    for i in cc:
        if i in vowels:
            n += 1
    sent.append(n - 1)
    words = cc.split()
    word_len = []
    word_vow = []
    for word in words:
        word_len.append(len(word))
        n2 = 0
        for w in word:
            if w in vowels:
                n2 += 1
        word_vow.append(n2)
    sent.append(np.median(word_len) - 1)
    sent.append(np.median(word_vow) - 1)
    if True not in np.isnan(sent):
        sonets.append(sent)

anna = []
for c in corpus2:
    sent = []
    cc = re.sub('(,|:|;|\r\n|")', '', c.lower())
    sent.append(len(re.sub(' ', '', cc)) - 1)
    sent.append(len(''.join(set(re.sub(' ', '', cc)))) - 1)
    n = 0
    for i in cc:
        if i in vowels:
            n += 1
    sent.append(n - 1)
    words = cc.split()
    word_len = []
    word_vow = []
    for word in words:
        word_len.append(len(word))
        n2 = 0
        for w in word:
            if w in vowels:
                n2 += 1
        word_vow.append(n2)
    sent.append(np.median(word_len) - 1)
    sent.append(np.median(word_vow) - 1)
    if True not in np.isnan(sent):
        anna.append(sent)

anna_data = np.array(anna)
sonets_data = np.array(sonets)
#plt.figure()
#c1, c2 = 0, 1
#plt.plot(anna_data[:,c1], anna_data[:,c2], 'og', 
#         sonets_data[:,c1], sonets_data[:,c2], 'sb')
#plt.show()

#p = mlab.PCA(anna_data, True)
#plt.plot(p.Y[:,0], p.Y[:,1], 'o')
#plt.show()

data = np.vstack((anna_data, sonets_data))
p = mlab.PCA(data, True)
N = len(anna_data)
plt.plot(p.Y[:N,0], p.Y[:N,1], 'og', p.Y[N:,0], p.Y[N:,1], 'sb')
plt.show()

parameters = {'C': (.1, .5, 1.0, 1.5, 1.7, 2.0)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)
gs.fit(data[:, 1:], data[:, 0])
clf = svm.LinearSVC(C=gs.best_estimator_.C)
clf.fit(data[::2, 1:], data[::2, 0])

wrong = 0
for obj in data[1::2, :]:
    label = clf.predict(obj[1:])
    if label != obj[0] and wrong < 3:
        print('Пример ошибки машины: class = ', obj[0], ', label = ', label, ', экземпляр ', obj[1:])
        wrong += 1
    if wrong > 3:
        break

    
    

