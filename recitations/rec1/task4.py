import random
from pyspark import SparkContext
from operator import add

NUM_SAMPLES=10000000

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

sc = SparkContext(appName="Pi")
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))