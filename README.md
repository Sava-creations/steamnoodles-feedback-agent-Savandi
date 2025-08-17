Customer Feedback Response Agent

Name: Savandi Kodithuwakku
University: University of Moratuwa
Year: 2nd Year

Summary of Approach

The Customer Feedback Response Agent is a Python application that:

Accepts individual customer feedback as input.

Uses a pre-trained HuggingFace Transformer model (nlptown/bert-base-multilingual-uncased-sentiment) to determine the sentiment of the feedback: positive, negative, or neutral.

Generates a short, polite, and context-aware automated reply based on the detected sentiment.

Displays the review, detected sentiment, and auto-reply in a user-friendly GUI using Tkinter.

Allows the user to iterate through a dataset of restaurant reviews.

Sentiment Mapping:

4–5 stars → Positive

3 stars → Neutral

1–2 stars → Negative

Instructions to Test the Agent

Install required libraries:

pip install pandas transformers torch tkinter


Note: tkinter comes with Python by default, so it may already be installed.

Place the dataset

Make sure the TSV dataset file (Restaurant_Reviews.tsv) is in the data folder.

The dataset should have the following columns:

Review → Customer feedback text

Liked → 1 for positive, 0 for negative

Run the script:

python agents/feedback_agent.py


Use the GUI:

The first review will be displayed automatically.

The detected sentiment and auto-generated reply will appear below the review.

Click Next Review to view the next review from the dataset.

Notes

The agent can handle multiple reviews from the dataset, and the GUI allows easy navigation.

The sentiment analysis model is multilingual and pre-trained on restaurant reviews, making it suitable for this task
