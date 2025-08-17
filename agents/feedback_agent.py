# from transformers import pipeline

# # # Load sentiment-analysis pipeline
# # sentiment_analyzer = pipeline("sentiment-analysis")

# sentiment_analyzer = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english",
#     revision="714eb0f"
# )

# def generate_reply(review_text):
#     # Analyze sentiment
#     result = sentiment_analyzer(review_text)[0]
#     label = result['label']  # 'POSITIVE' or 'NEGATIVE'
    
#     # Generate polite reply
#     if label == 'POSITIVE':
#         reply = f"Thank you for your kind words! We're glad you enjoyed: \"{review_text}\""
#     elif label == 'NEGATIVE':
#         reply = f"Sorry to hear about your experience: \"{review_text}\". We will try to improve."
#     else:
#         reply = f"Thank you for your feedback: \"{review_text}\"."
    
#     return reply

# # Example usage
# sample_review = "The food was amazing and the service was excellent!"
# reply = generate_reply(sample_review)
# print("Sample review:", sample_review)
# print("Auto-reply:", reply)


# from transformers import pipeline

# # # Load sentiment-analysis pipeline
# # sentiment_model = pipeline("sentiment-analysis")

# sentiment_pipeline = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def generate_reply(feedback_text):
#     result = sentiment_pipeline(feedback_text)[0]
#     sentiment = result['label']  # 'POSITIVE' or 'NEGATIVE'
    
#     # Map HuggingFace labels to your format
#     if sentiment == "POSITIVE":
#         sentiment_label = "positive"
#         reply = f"Thank you for your kind words! We're glad you enjoyed: \"{feedback_text}\""
#     elif sentiment == "NEGATIVE":
#         sentiment_label = "negative"
#         reply = f"We're sorry for your experience. Thank you for your feedback: \"{feedback_text}\""
#     else:
#         sentiment_label = "neutral"
#         reply = f"Thank you for your feedback: \"{feedback_text}\""
    
#     return sentiment_label, reply

# # Example
# sample_review = "The food was amazing and the service was excellent!"
# sentiment, reply = generate_reply(sample_review)
# print("Detected sentiment:", sentiment)
# print("Auto-reply:", reply)

# from transformers import pipeline

# # Load the multilingual sentiment model
# sentiment_pipeline = pipeline(
#     "sentiment-analysis",
#     model="nlptown/bert-base-multilingual-uncased-sentiment"
# )

# def generate_reply(feedback_text):
#     result = sentiment_pipeline(feedback_text)[0]
#     label = result['label']  # '1 star' to '5 stars'

#     # Map into sentiment categories
#     if label in ['4 stars', '5 stars']:
#         sentiment = "positive"
#         reply = f"Thank you for your kind words! We're glad you enjoyed: \"{feedback_text}\""
#     elif label == '3 stars':
#         sentiment = "neutral"
#         reply = f"Thank you for your honest feedback: \"{feedback_text}\""
#     else:  # 1 or 2 stars
#         sentiment = "negative"
#         reply = f"We're sorry for your experience. Thank you for your feedback: \"{feedback_text}\""

#     return sentiment, reply

# # Example usage
# sample_reviews = [
#     "The food and service were outstanding.",
#     "It was okay, nothing special.",
#     "The food was cold and the service was slow."
# ]

# for review in sample_reviews:
#     sentiment, reply = generate_reply(review)
#     print("Review:", review)
#     print("Detected sentiment:", sentiment)
#     print("Auto-reply:", reply)
#     print("-" * 60)

import pandas as pd
from transformers import pipeline
import tkinter as tk
from tkinter import ttk, messagebox

# Load the dataset
dataset_path = "data/Restaurant_Reviews.tsv"  # adjust if needed
df = pd.read_csv(dataset_path, sep='\t')  # TSV file

# Load sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Function to generate sentiment and reply
def generate_reply(feedback_text):
    result = sentiment_pipeline(feedback_text)[0]
    label = result['label']

    if label in ['4 stars', '5 stars']:
        sentiment = "positive"
        reply = f"Thank you for your kind words! We're glad you enjoyed: \"{feedback_text}\""
    elif label == '3 stars':
        sentiment = "neutral"
        reply = f"Thank you for your honest feedback: \"{feedback_text}\""
    else:
        sentiment = "negative"
        reply = f"We're sorry for your experience. Thank you for your feedback: \"{feedback_text}\""

    return sentiment, reply

# GUI
class FeedbackApp:
    def __init__(self, master):
        self.master = master
        master.title("Customer Feedback Agent")
        master.geometry("700x400")

        self.index = 0  # current review index

        # Review display
        self.review_label = ttk.Label(master, text="Review:", font=("Arial", 12))
        self.review_label.pack(pady=10)

        self.review_text = tk.Text(master, wrap='word', height=5, width=80)
        self.review_text.pack()

        # Sentiment display
        self.sentiment_label = ttk.Label(master, text="", font=("Arial", 12, 'bold'))
        self.sentiment_label.pack(pady=10)

        # Auto-reply display
        self.reply_text = tk.Text(master, wrap='word', height=5, width=80)
        self.reply_text.pack()

        # Buttons
        self.next_button = ttk.Button(master, text="Next Review", command=self.next_review)
        self.next_button.pack(pady=10)

        # Load first review
        self.load_review()

    def load_review(self):
        if self.index >= len(df):
            messagebox.showinfo("End", "No more reviews in the dataset.")
            self.master.quit()
            return

        review = df.iloc[self.index]['Review']  # adjust column name if different
        self.review_text.delete(1.0, tk.END)
        self.review_text.insert(tk.END, review)

        sentiment, reply = generate_reply(review)
        self.sentiment_label.config(text=f"Detected Sentiment: {sentiment}")
        self.reply_text.delete(1.0, tk.END)
        self.reply_text.insert(tk.END, reply)

    def next_review(self):
        self.index += 1
        self.load_review()

# Run GUI
root = tk.Tk()
app = FeedbackApp(root)
root.mainloop()
