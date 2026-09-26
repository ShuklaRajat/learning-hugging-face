# Grammatical correctness

# Text classification is the process of labeling an input text into a
# pre-defined category. Examples include sentiment analysis (positive
# or negative), spam detection (spam or not spam), and grammatical
# error detection.

# In this exercise, use a "text-classification" pipeline to check
# whether an input sentence is grammatically correct.

# The "pipeline" function from the "transformers" library is already
# loaded for you.

# Instructions:
# - Create a pipeline for the "text-classification" task using the
#   "abdulmatinomotoso/English_Grammar_Checker" model.
# - Save the pipeline as "grammar_checker".
# - Use "grammar_checker" to predict the grammatical correctness
#   of the provided input sentence.
# - Save the prediction as "output".

from transformers import pipeline

# Create a pipeline for grammar checking
pipe = pipeline(
  task="text-classification", 
  model="abdulmatinomotoso/English_Grammar_Checker"
)

# Check grammar of the input text
output = pipe("I will walk dog")
print(output)


#<script.py> output:
#    [{'label': 'LABEL_0', 'score': 0.9956323504447937}]