# Question Natural Language Inference (QNLI)

# QNLI is a text classification task that determines whether a
# given premise contains enough information to answer a question.
#
# Different text classification tasks can be performed by using
# different pretrained models. Each model is trained to predict
# specific labels based on the context of the input text.
#
# The "pipeline" function from the "transformers" library is
# already loaded for you.

# Instructions:
# - Create a text classification pipeline for QNLI using the
#   "cross-encoder/qnli-electra-base" model.
# - Save the pipeline as "classifier".
# - Use the classifier to determine whether the provided text
#   contains enough information to answer the given question.

from transformers import pipeline

# Create the pipeline
classifier = pipeline(____="text-classification" , ____="cross-encoder/qnli-electra-base")

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.")

print(output)