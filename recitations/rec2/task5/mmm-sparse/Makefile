EXAMPLE_DIR = /user/$(USER)/task5
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
# add hadoop version
HADOOP_VERSION = 3.1.1

# check $HADOOP_HOME with echo $HADOOP_HOME
HADOOP_HOME='/usr/local/Cellar/hadoop/3.1.1/libexec/'
TOOLLIBS_DIR=$(HADOOP_HOME)/share/hadoop/tools/lib/
NITERS=25

run: inputs
	hdfs dfs -rm -f -r $(OUTPUT_DIR) 
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./sparse-map.py,./sparse-reduce.py \
		-mapper ./sparse-map.py  -reducer ./sparse-reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR)
	hdfs dfs -cat $(OUTPUT_FILE) > sparse-mmm
	cat sparse-mmm

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir -p $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir -p $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir -p $(OUTPUT_DIR)

inputs: directories
	hdfs dfs -test -e $(INPUT_DIR)/part-00000 \
	  || hdfs dfs -put ./input/part-00000 $(INPUT_DIR)/part-00000

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -f -r $(EXAMPLE_DIR)
	-rm -f sparse-mmm

.PHONY: directories inputs clean run 
