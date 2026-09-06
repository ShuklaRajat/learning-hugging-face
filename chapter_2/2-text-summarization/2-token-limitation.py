# Adjusting the summary length

# The pipeline() function provides two important parameters for
# controlling the length of generated summaries:
# - min_new_tokens: specifies the minimum number of new tokens
#   the model should generate.
# - max_new_tokens: specifies the maximum number of new tokens
#   the model can generate.
#
# These parameters can be used to create shorter or longer summaries
# depending on requirements such as storage limitations, readability,
# or summary quality.
#
# The "pipeline" function from the "transformers" library and
# "original_text" have already been loaded for you.

# Instructions - Part 1:
# - Create a summarization pipeline that summarizes "original_text"
#   to between 1 and 10 tokens.


# Generate a summary of original_text between 1 and 10 tokens
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=1, max_new_tokens=10)

short_summary_text = short_summarizer(original_text)

print(short_summary_text[0]["summary_text"])

#
# Instructions - Part 2:
# - Repeat the same steps using a summarization pipeline with a
#   minimum length of 50 tokens and a maximum length of 150 tokens.

# Repeat for a summary between 50 and 150 tokens
long_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=50, max_new_tokens=150)

long_summary_text = long_summarizer(original_text)

print(long_summary_text[0]["summary_text"])