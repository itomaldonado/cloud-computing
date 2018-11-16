#!/usr/bin/python

import sys
import collections

counter = collections.Counter()

for line in sys.stdin:
    k, v = line.strip().split("\t", 2)

    counter[k] += int(v)

for k,v in counter.most_common(100):
  print('{0}\t{1}'.format(k,v))
