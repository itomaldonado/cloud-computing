#!/usr/bin/env python

import sys
import numpy


def generate_data(matrix, m, n):
    density = m * n
    rand_seq = numpy.random.permutation(m*n)[:density]
    row  = rand_seq / n
    col  = rand_seq % n
    vals = numpy.random.randn(density, 1)

    # create placeholder dictionaries
    mat = [ {} for _ in range(0,m) ]

    for i in range(0,density):
      # dereference the numpy array
      mat[int(row[i])][int(col[i])] = vals[i][0]

    for rowid,vals in enumerate(mat):
      for col,val in vals.items():
          print(matrix, rowid, col, val)

if __name__ == '__main__':
    if len(sys.argv) != 3:
      print("python %s <number_rows> <number_columns>" % (sys.argv[0]), file=sys.stderr)
      sys.exit(-1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])

    generate_data('A', m, n)
    generate_data('B', m, n)
