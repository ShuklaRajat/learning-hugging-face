# Loading datasets

# After choosing a dataset, load it using the "datasets" library.
#
# In this exercise, load the "TIGER-Lab/MMLU-Pro" dataset.
# The dataset is a benchmark evaluation dataset.
#
# The load_dataset function from the "datasets" package
# is already loaded for you.

# Instructions:
# - Use the correct function to load the "TIGER-Lab/MMLU-Pro" dataset.
# - Specify the "validation" split.

from datasets import load_dataset

# Load the "validation" split of the TIGER-Lab/MMLU-Pro dataset
my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="validation")

# Display dataset details
print(my_dataset)