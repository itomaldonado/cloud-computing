import pyspark
sc = pyspark.SparkContext('local[*]')
rdd = sc.parallelize(range(1000))
print(rdd.takeSample(False, 5))
sc.stop()  # stop the spark context