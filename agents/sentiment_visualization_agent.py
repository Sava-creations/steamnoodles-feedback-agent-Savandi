import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

dataset_path = "data/Restaurant_Reviews.tsv"
df = pd.read_csv(dataset_path, sep='\t')  

# Convert timestamp to datetime if needed
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

def map_sentiment(row):
    if row['Liked'] == 1:
        return 'positive'
    elif row['Liked'] == 0:
        return 'negative'
    else:
        return 'neutral'

df['Sentiment'] = df.apply(map_sentiment, axis=1)

start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

mask = (df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)
df_filtered = df.loc[mask]

daily_counts = df_filtered.groupby(['Timestamp', 'Sentiment']).size().unstack(fill_value=0)

daily_counts.plot(kind='bar', stacked=True, figsize=(12,6))
plt.title("Daily Sentiment Counts")
plt.xlabel("Date")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.show()
