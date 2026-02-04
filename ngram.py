from nltk import bigrams
from collections import Counter

text = "i love pizza i love cake i hate vegatables"
tokens = text.split()

bi_list = list(bigrams(tokens))
bi_count = Counter(bi_list)

# Get bigrams where the first word is 'i'
res = {pair[1]: count for pair, count in bi_count.items() if pair[0] == 'i'}
print(res)