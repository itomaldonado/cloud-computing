#!/usr/bin/python

import sys

current_key = None
current_count = 0
key = None

for line in sys.stdin:
    key, value = line.strip().split('\t')
    try:
        value = float(value)
    except ValueError:  
        continue
    if current_key == key:
        current_count += value
    else:
        if current_key:
            print("%s\t%s" % (current_key, current_count))
        current_count = value
        current_key = key

if key == current_key:  
    print("%s\t%s" % (current_key, current_count))
