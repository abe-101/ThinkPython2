""" Count total number of words and word frequency in a file. """
import string
from operator import itemgetter
from collections import Counter

with open('test_book.txt', encoding='UTF-8') as f:
    strippables = string.punctuation + string.whitespace
    cnt = Counter()
    for line in f:
        for word in line.split():
            word = word.strip(strippables).lower()
            cnt[word] += 1

    words_total = (sum(cnt.values()))

    print("Total number of words: ", words_total)
    print("Word frequency:")

    for word, freq in sorted(cnt.items(), key=itemgetter(1), reverse=True):
        print(f'{word:15} ==> {freq:5}')
