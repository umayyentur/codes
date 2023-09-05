import pandas as pd
import nltk
from nltk.corpus import stopwords
from textblob import Word
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

data = pd.read_csv("/Users/umayyentur/Downloads/DataSets/IphoneData.csv", sep="\t")
tweets = data["Reviews"]

stp = stopwords.words("english")
tweets = tweets.apply(lambda x: " ".join(str(item).lower() for item in str(x).split()))
tweets = tweets.str.replace("[^\w\s]", "")
tweets = tweets.str.replace("\d", "")
tweets = tweets.apply(lambda x: " ".join(x for x in x.split() if x not in stp))
tweets = tweets.apply(lambda x: " ".join(Word(i).lemmatize() for i in x.split()))


frekanslar = tweets.str.split(expand=True).stack().value_counts().reset_index()
frekanslar.columns = ["Kelime", "Frekans"]



tweet_proc = " ".join(tweets)

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ["Negative", "Neutral", "Positive"]

max_length = 128  
encoded_tweet = tokenizer(tweet_proc, return_tensors="pt", truncation=True, padding=True, max_length=max_length)

output = model(**encoded_tweet)
logits = output.logits

probabilities = torch.softmax(logits, dim=1)

predicted_class = torch.argmax(probabilities, dim=1).item()

predicted_label = labels[predicted_class]
print(f"Predicted Sentiment: {predicted_label}")
print("Sentiment Probabilities:")
for i, label in enumerate(labels):
    probability = probabilities[0][i].item()
    print(f"{label}: {probability:.4f}")







