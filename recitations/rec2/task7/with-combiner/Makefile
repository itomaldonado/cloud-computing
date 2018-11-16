# User variables
HADOOP_PREFIX = /usr/local/Cellar/hadoop/3.1.1/libexec/
HADOOP_VERSION = 3.1.1
EXAMPLE_DIR = /user/$(USER)/with-combiner/
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
TOOLLIBS_DIR=$(HADOOP_PREFIX)/share/hadoop/tools/lib/

run: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) 
	hdfs dfs -cat $(OUTPUT_FILE) > top-100-words.txt
	cat top-100-words.txt

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir -p $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir -p $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir -p $(OUTPUT_DIR)

inputs: directories
	hdfs dfs -test -e $(INPUT_DIR)/words \
	  || hdfs dfs -put ../input/words $(INPUT_DIR)/words

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -r -f $(EXAMPLE_DIR)
	-rm -f top-100-words.txt

.PHONY: directories inputs clean run
