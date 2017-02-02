import codecs
import nltk
from nltk.collocations import *
from nltk.metrics.spearman import *
import pymorphy2

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

morph = pymorphy2.MorphAnalyzer()
punct = '.,!?():;'
words = [word.strip(punct) for word in codecs.open('court-V-N.csv', 'r', 'utf-8').read().split()]
words[:] = [x for x in words if x != 'СУД']          
words_tagged = [morph.parse(word)[0].normal_form for word in words]


#Метрика - Log Likelihood

finder = BigramCollocationFinder.from_words(words_tagged)
#nltk.download()
stopwords = nltk.corpus.stopwords.words('russian')
finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in stopwords)
log_likelihood = finder.nbest(bigram_measures.likelihood_ratio, 10)
#print(finder.nbest(bigram_measures.likelihood_ratio, 10))

#Метрика - PMI

pmi = finder.nbest(bigram_measures.pmi, 10)
#print(finder.nbest(bigram_measures.pmi, 10))

#Сравнение с золотым стандартом

gold_file = codecs.open('gold.txt', 'r', 'utf-8')
gold = []
for line in gold_file:
    line = line.strip()
    words = line.split()
    t = [words[0], words[1]]
    gold.append(tuple(t))

#print(gold)

#Log Likelihood

print('%0.1f' % spearman_correlation(ranks_from_sequence(log_likelihood), ranks_from_sequence(gold)))

#PMI

print('%0.1f' % spearman_correlation(ranks_from_sequence(pmi), ranks_from_sequence(gold)))

#Ранжированные списки, созданные по метрикам Log Likelihood и PMI, плохо отражают золотой стандарт.
#Но мои биграммы включают в себя не только решения суда (глагол + сущ).
#Поэтому это можно было ожидать. В целом метрика Log Likelihood лучше определила ранги, так как с=биграммы повторялись, но не на тех местах.


