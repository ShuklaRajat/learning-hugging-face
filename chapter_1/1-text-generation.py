# Building a text generation pipeline

# Hugging Face pipelines make it simple to use machine learning models
# for a variety of tasks. In this exercise, you'll build a text generation
# pipeline using the "gpt2" model and customize the output by adjusting
# its parameters.

# Feel free to experiment with different prompts in the pipeline, such as
# "What if ...?", "How to ...?", or any other creative idea you'd like
# to explore.

# Instructions:
# - Complete the missing code to build a text generation pipeline using
#   the "gpt2" model.
# - Provide a custom sentence of your choice as the input prompt.
# - Keep the prompt short to prevent timeouts.
# - Configure the pipeline to generate up to 10 tokens.
# - Configure the pipeline to produce 2 outputs.

from transformers import pipeline 

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")

# Generate three text outputs with a maximum length of 10 tokens
results = gpt2_pipeline("What if AI", max_new_tokens=10, num_return_sequences=2)

for result in results:
    print(result['generated_text'])