#!/usr/bin/env python

import sys
from operator import itemgetter

prev_index = None
value_list = []

values_from_A = []
values_from_B = []

for line in sys.stdin:
    j, matrix, i_k, value = line.rstrip().split("\t")
    j, matrix, i_k, value = line.rstrip().split("\t")
    j, i_k = map(int,[j, i_k])
    value = float(value)
    if matrix == 'A':
        values_from_A.append((i_k,value))
    elif matrix == 'B':
        values_from_B.append((i_k,value))

for (i, value_1) in values_from_A:
    for (k, value_2) in values_from_B:
        key = '{0},{1}'.format(i,k)
        print('{0}\t{1}'.format(key, (value_1*value_2)))
