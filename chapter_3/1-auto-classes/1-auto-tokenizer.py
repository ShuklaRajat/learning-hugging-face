# Tokenizing text with AutoTokenizer

# AutoTokenizer simplifies text preparation by automatically handling
# tasks such as cleaning, normalization, and tokenization.
#
# It ensures that the text is processed in the same way that the
# corresponding pretrained model expects.
#
# In this exercise, explore how AutoTokenizer transforms input text
# into tokens that can be used for machine learning tasks.

# Instructions:
# - Import the required class from the "transformers" library.
# - Load the tokenizer using the correct method.
# - Split the input text into tokens.

# Import necessary library for tokenization
from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Split input text into tokens
tokens = tokenizer.tokenize("AI: Making robots smarter and humans lazier!")

# Display the tokenized output
print(f"Tokenized output: {tokens}")

# okenized output: ['ai', ':', 'making', 'robots', 'smarter', 'and', 'humans', 'la', '##zier', '!']