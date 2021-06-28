import pathlib
import logging
import os

# Importing the solution
from solution import find_common_node

# Setup Logger and log to a file
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='test_results.log',
                    level=logging.DEBUG)

logging.info("\n")
logging.info(("==== " * 4) + "Starting New Run " + ("==== " * 4))

# Globals
DATASET_PATH = os.path.join("/home/anilkumar/Desktop/TechQWareLabsPythonTest_Ans", "data.txt")
logging.info("Loading dataset from : ")
logging.warning("%s",DATASET_PATH)

# Test Results
samples_to_evaluate = [{
    "node_a": 100,
    "node_b": 200,
    "expected_label": 5,
}, {
    "node_a": 128,
    "node_b": 130,
    "expected_label": 113,
}, {
    "node_a": 86,
    "node_b": 76,
    "expected_label": 918,
}, ]

for sample_index, sample in enumerate(samples_to_evaluate):
    node_a = sample["node_a"]
    node_b = sample["node_b"]
    expected_label = sample["expected_label"]
    # logging.info("sample #{sample_index}: node_a={node_a}, node_b={node_b}")
    logging.warning("sample index = %s   node_a = %s   node = %s " ,sample_index,node_a,node_b)
    actual_label = find_common_node(data_set_path=DATASET_PATH,
                                    node_a=node_a,
                                    node_b=node_b)
    if type(actual_label) != int:
        # logging.warning(
        #     "The expected label should be `int`, instead received {type(actual_label).__name__}")
        actual_label = int(actual_label)

    is_label_expected = actual_label == expected_label

    logging.log(level=20 if is_label_expected else 30,
                msg="expected={expected_label}, actual={actual_label")
    
    logging.warning("expected=%s, actual=%s",expected_label,actual_label)

# End Message
logging.info(("==== " * 2) + "Please do not delete this file or it's contents.")
logging.info(("==== " * 2) + "It's ok to keep the results of your multiple runs. "
                             "In such cases we will consider the last run.")
logging.info(("==== " * 4) + "Run Complete " + ("==== " * 4))
