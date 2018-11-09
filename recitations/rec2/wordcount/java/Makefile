EXAMPLE_DIR = /user/$(USER)/wordcount
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-r-00000

CLASSPATH=$(shell hadoop classpath)
# yarn.resourcemanager.address localhost:8088
# mapreduce.framework.name yarn
# fs.defaultFS hdfs://localhost:9870/
# fs.default.name localhost:9870
# mapred.job.tracker localhost:8088

run: wordcount.jar inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar wordcount.jar WordCount \
	       $(INPUT_DIR) $(OUTPUT_DIR)
	hdfs dfs -cat wordcount/output/"*"

wordcount.jar: WordCount.java
	mkdir -p wordcount_classes
	javac -classpath $(CLASSPATH) -Xlint:deprecation \
 	      -d wordcount_classes WordCount.java
	jar -cvf wordcount.jar -C wordcount_classes .

inputdir:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir -p $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir -p $(INPUT_DIR)

outputdir:
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir -p $(OUTPUT_DIR)

inputs: inputdir
	hdfs dfs -test -e $(INPUT_DIR)/file01 \
	  || hdfs dfs -put ../input-small/file01 $(INPUT_DIR)/file01
	hdfs dfs -test -e $(INPUT_DIR)/file02 \
	  || hdfs dfs -put ../input-small/file02 $(INPUT_DIR)/file02

clean:
	-rm *.jar
	-rm -r *_classes
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -f -r $(EXAMPLE_DIR)

.PHONY: clean run directories inputs
