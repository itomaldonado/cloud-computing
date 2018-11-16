#!/usr/bin/python

import sys

row_size_a = 100
col_size_b = 100

for line in sys.stdin:
    line = line.strip()
    matrix, row_no, col_no, val = line.split()

    if matrix is 'A':
        for i in range(col_size_b):
            key = row_no + "," + str(i)
            print('{0}\t{1}\t{2}'.format(key,col_no,val))
    else:
        for j in range(row_size_a):
            key = str(j) + "," + col_no
            print('{0}\t{1}\t{2}'.format(key,row_no,val))
