# Manipulating datasets

# Datasets often need to be manipulated before being used in ML tasks.
# Two common operations are filtering and selecting (or slicing).
#
# Hugging Face uses Apache Arrow file types to efficiently handle
# large datasets, so dataset manipulations are performed using
# built-in methods rather than standard Python list operations.
#
# The dataset is already loaded for you under the variable "wikipedia".

# Instructions:
# - Filter the dataset for rows where the "text" column contains
#   the term "football" and save the result as "filtered".
# - Select a single example from the filtered dataset and save it
#   as "example".

# Filter the documents
filtered = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = filtered.select(range(1))

print(example[0]["text"])

