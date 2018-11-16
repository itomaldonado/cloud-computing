#!/usr/bin/python

import sys

row_size_a = 100
col_size_b = 100

for line in sys.stdin:
    line = line.strip()
    matrix, row_no, col_no, val = line.split()
    val = float(val)

    if matrix is 'A':
        print('{0}\t{1}\t{2}\t{3}'.format(col_no, matrix, row_no, val))
    else:
        print('{0}\t{1}\t{2}\t{3}'.format(row_no, matrix, col_no, val))
