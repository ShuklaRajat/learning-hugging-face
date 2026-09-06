# Dynamic category assignment

# Zero-shot classification allows a model to classify text into
# predefined categories without requiring prior training specifically
# for those categories.
#
# Using Hugging Face's pipeline() with the "zero-shot-classification"
# task, provide the input text and a list of predefined categories.
# The model will determine which category best matches the text.
#
# The "pipelines" module from the "transformers" library is already
# loaded for you.
#
# Note:
# A customized version of the pipeline is being used so that you
# can learn how to use these functions without downloading the model.

# Instructions:
# - Build a zero-shot classification pipeline and save it as "classifier".
# - Create a list of categories: "politics", "science", and "sports".
# - Save the categories as "categories".
# - Use "classifier" to predict the label of "text" using the
#   predefined categories.

from transformers import pipeline

text = "AI-powered robots assist in complex brain surgeries with precision."

# Create the pipeline
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the categories list
categories = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, categories)

# Print the top label and its score
print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")


#<script.py> output:
#    Top Label: science with score: 0.9510332942008972