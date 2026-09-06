# Summarizing long text

# Summarization reduces large amounts of text into shorter, more
# manageable content, allowing readers to quickly understand the
# key points of lengthy articles or documents.
#
# There are two main types of summarization:
# - Extractive summarization selects important sentences from the
#   original text.
# - Abstractive summarization generates new sentences that rephrase
#   and summarize the main ideas.
#
# In this exercise, create an abstractive summarization pipeline
# using Hugging Face's pipeline() function and the
# "cnicu/t5-small-booksum" model.
#
# The pipeline function from the "transformers" library and the
# "original_text" have already been loaded for you.
#
# Instructions:
# - Create a summarization pipeline using the "summarization" task
#   and save it as "summarizer".
# - Use the new pipeline to create a summary of "original_text"
#   and save it as "summary_text".
# - Compare the length of the original text with the length of
#   the summary text.

# Create the summarization pipeline
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")


#Original text length: 829
#Summary length: 473