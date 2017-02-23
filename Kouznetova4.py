from nltk.corpus import wordnet
import nltk

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

# 4)    Найдите гиперонимы для значения (a) и гиперонимы для значения (b)

print('a)')
print(set1.hypernyms())
print('b)')
print(set2.hyponyms())
print('')

# 5)    Вычислите наименьшее расстояние между значением plant "завод" и значениями лексемы industry, а также plant "растение" и значениями лексемы leaf

industry = wordnet.synsets('industry')


