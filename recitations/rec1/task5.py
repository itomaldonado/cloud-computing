from pyspark import SparkContext

# Insert your own code, transform the code below:
sc = SparkContext(appName="Spark_Messages")
lines = sc.textFile("file01_Hd_Sp_Freq")

# transformed RDDs
messages = lines.filter(lambda line: line.startswith('I')).map(lambda line: line.split('\n')).map(lambda word: (word, 1))
messages.cache()
print(messages.filter(lambda message: 'Spark' in message[0][0]).count())
sc.stop()