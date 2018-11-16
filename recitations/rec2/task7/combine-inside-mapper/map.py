#!/usr/bin/python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words: 
        count = 1

        #inside combiner
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print("%s\t%s" % (current_word, current_count))
            current_count = count
            current_word = word

if word == current_word:  
    print("%s\t%s" % (current_word, current_count))

