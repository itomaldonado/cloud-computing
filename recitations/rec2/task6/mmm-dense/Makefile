EXAMPLE_DIR = /user/$(USER)/dense-mmm
INPUT_DIR   = $(EXAMPLE_DIR)/input
MID_OUTPUT_DIR  = $(EXAMPLE_DIR)/mid-output
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
# add hadoop version
HADOOP_VERSION = 3.1.1

# check $HADOOP_HOME with echo $HADOOP_HOME
HADOOP_HOME='/usr/local/Cellar/hadoop/3.1.1/libexec/'
TOOLLIBS_DIR=$(HADOOP_HOME)/share/hadoop/tools/lib/

run: inputs
	hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hdfs dfs -rm -f -r $(MID_OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map-1.py,./reduce-1.py \
		-mapper ./map-1.py  -reducer ./reduce-1.py \
		-input $(INPUT_DIR) \
		-output  $(MID_OUTPUT_DIR)
	hdfs dfs -rm $(MID_OUTPUT_DIR)/_SUCCESS
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map-2.py,./reduce-2.py \
		-mapper ./map-2.py  -reducer ./reduce-2.py \
		-input $(MID_OUTPUT_DIR) \
		-output  $(OUTPUT_DIR)
	hdfs dfs -cat $(OUTPUT_FILE) > mmm-data
	cat mmm-data

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir -p $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir -p $(INPUT_DIR)
	hdfs dfs -test -e $(MID_OUTPUT_DIR) || hdfs dfs -mkdir -p $(MID_OUTPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir -p $(OUTPUT_DIR)

inputs: directories
	hdfs dfs -test -e $(INPUT_DIR)/mmm-data \
	  || hdfs dfs -put ./input/mmm-data $(INPUT_DIR)/mmm-data

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(MID_OUTPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -f -r $(EXAMPLE_DIR)
	-rm -f mmm-data

.PHONY: directories inputs clean run 
