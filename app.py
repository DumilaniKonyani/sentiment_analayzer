#import textblob

from textblob import TextBlob

# review samples
reviews = [
    "I love this laptop!",
"Do I really love this laptop?",
"I don't really love this laptop!",
"Worst laptop ever",
"best laptop ever",
    "I'm not sure if I love this laptop or not"
]

# analyse sentiments
for review in reviews:
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity #-1 (negative) to +1 (positive)

    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    print(f"Review: \"{review}\" Sentiment: {sentiment_label}")