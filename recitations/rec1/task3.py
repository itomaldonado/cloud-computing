from pyspark import SparkContext
from operator import add

sc = SparkContext(appName="Top_Words")
lines = sc.textFile("file01_Hd_Sp_Freq")

# counts is an RDD of the form (word, count)
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(add)

# collect brings it to a list in local memory and you can extract info in the form of (word, count)
output = counts.collect()
output.sort(key=lambda tup: tup[1], reverse=True)
print(output[:3])

sc.stop()  # stop the spark context