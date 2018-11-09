import os
import shutil

from pyspark import SparkContext
from operator import add

## If file exists, delete it ##
if os.path.isdir("wc_out.txt"):
    shutil.rmtree("wc_out.txt")
else:    ## Show an error ##
    print("Error: %s file not found" % "wc_out.txt")

sc = SparkContext('local[*]')
f = sc.textFile("file01_Hd_Sp_Freq")

wc = f.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

wc.saveAsTextFile("wc_out.txt")

sc.stop()  # stop the spark context