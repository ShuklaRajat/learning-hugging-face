# Using AutoClasses

# AutoClasses allow you to automatically load the appropriate model
# architecture and tokenizer for a specific pretrained model.
#
# Here, AutoModelForSequenceClassification is used for the sentiment
# analysis task, while AutoTokenizer prepares the input text in the
# format expected by the model.
#
# Combining AutoClasses with pipeline() provides a balance between
# control over the model/tokenizer and the convenience of pipelines.
#
# The following have already been imported from "transformers":
# - AutoModelForSequenceClassification
# - AutoTokenizer
# - pipeline
#
# Instructions:
# - Download the pretrained model and save it as "my_model".
# - Download the corresponding tokenizer and save it as "my_tokenizer".
# - Create a sentiment analysis pipeline using the model and tokenizer
#   and save it as "my_pipeline".
# - Use "my_pipeline" to predict the sentiment of the provided input
#   and save the result as "output".
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Download the model and tokenizer
my_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
my_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# Predict the sentiment
output = my_pipeline("This course is pretty good, I guess.")
print(f"Sentiment using AutoClasses: {output[0]['label']}")

#     Sentiment using AutoClasses: POSITIVE