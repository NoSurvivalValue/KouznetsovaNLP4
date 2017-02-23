from nltk.corpus import wordnet
import nltk
from nltk.wsd import lesk

# 1)    Найти все значения (синсеты) для лексемы plant

#nltk.download()
print(wordnet.synsets('plant'))
print('')

# 2)    Найти определение
#       для лексемы plant в значении (а) "завод" и в значении (b) "растение"

set1 = wordnet.synset('plant.n.01')
print('a)')
print(set1.definition())
set2 = wordnet.synset('plant.n.02')
print('b)')
print(set2.definition())
print('')

# 3)    Найдите два произвольных контекста для слова plant
#       в значениях (a) "завод" и (b) "растение";
#       продемонстрируйте на них действие алгоритма Леска для разрешения неоднозначности

sent1 = ['There', 'is', 'a', 'power', 'plant', 'across', 'the', 'street', 'from', 'our', 'house', '.']
sent2 = ['Please', 'water', 'the', 'plant', 'while', 'I', 'am', 'gone', '.']
print('a)')
print(lesk(sent2, 'plant').definition())
print('b)')
print(lesk(sent1, 'plant').definition())
print('')

# 4)    Найдите гиперонимы для значения (a) и гиперонимы для значения (b)

print('a)')
print(set1.hypernyms())
print('b)')
print(set2.hyponyms())
print('')

# 5)    Вычислите наименьшее расстояние между значением plant "завод" и значениями лексемы industry, а также plant "растение" и значениями лексемы leaf

#print(wordnet.synsets('industry'))
#print(wordnet.synsets('leaf'))
print('a)')
print(min(wordnet.synset('industry.n.01').path_similarity(set1), wordnet.synset('industry.n.02').path_similarity(set1),
          wordnet.synset('diligence.n.02').path_similarity(set1), wordnet.synset('leaf.n.01').path_similarity(set1),
          wordnet.synset('leaf.n.02').path_similarity(set1), wordnet.synset('leaf.n.03').path_similarity(set1),
          wordnet.synset('flick.v.02').path_similarity(set1), wordnet.synset('leaf.v.02').path_similarity(set1),
          wordnet.synset('leaf.v.03').path_similarity(set1)))
print('b)')
print(min(wordnet.synset('industry.n.01').path_similarity(set2), wordnet.synset('industry.n.02').path_similarity(set2),
          wordnet.synset('diligence.n.02').path_similarity(set2), wordnet.synset('leaf.n.01').path_similarity(set2),
          wordnet.synset('leaf.n.02').path_similarity(set2), wordnet.synset('leaf.n.03').path_similarity(set2),
          wordnet.synset('flick.v.02').path_similarity(set2), wordnet.synset('leaf.v.02').path_similarity(set2),
          wordnet.synset('leaf.v.03').path_similarity(set2)))
print('')

# 6)    Вычислить двумя разными способами расстояние: d(plant: "растение", rattlesnake's master) и d(organism, whole)

#print(wordnet.synsets('dandelion'))
#print(wordnet.synsets('whole'))
#print(wordnet.synsets('organism'))
print('a)')
print(wordnet.synset('dandelion.n.01').lch_similarity(set2))
print(min(wordnet.synset('whole.n.01').lch_similarity(wordnet.synset('organism.n.01')),
          wordnet.synset('whole.n.02').lch_similarity(wordnet.synset('organism.n.01')),
          wordnet.synset('whole.n.01').lch_similarity(wordnet.synset('organism.n.02')),
          wordnet.synset('whole.n.02').lch
          _similarity(wordnet.synset('organism.n.02'))))
print('b)')
print(wordnet.synset('dandelion.n.01').path_similarity(set2))
print(min(wordnet.synset('whole.n.01').path_similarity(wordnet.synset('organism.n.01')),
          wordnet.synset('whole.n.02').path_similarity(wordnet.synset('organism.n.01')),
          wordnet.synset('whole.n.01').path_similarity(wordnet.synset('organism.n.02')),
          wordnet.synset('whole.n.02').path_similarity(wordnet.synset('organism.n.02'))))

#Мне и там, и там кажется, что вид растения и растение должны быть ближе, чем очень абстрактоное "whole" и термин "organism". Поэтому оба способа мои догадки не подтверждают. 

