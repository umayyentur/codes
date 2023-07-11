from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

#tweet = "@umayyentur yesterday is hot @ hotelroom 🙂 https://dovizborsa.com "
tweet = "bad content! unsubscribed 😤"


#precprecess tweet
tweet_words = []

for word in tweet.split(" "):
    if word.startswith("@") and len(word) > 1:
        word = "@user"
        
    elif word.startswith("http"):
        word = "http"
    tweet_words.append(word)
          
tweet_proc = " ".join(tweet_words)
print(tweet_proc)

# modeli ve tokenizer indiriyoruz
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ["Negative", "Neutral" ,"Positive"]

#Dusunce analizi
encoded_tweet = tokenizer(tweet_proc, return_tensors="pt")
#output = model(encoded_tweet["input_ids"] , encoded_tweet["attention_mask"])

output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)

for i in range(len(scores)):
    l = labels[i]
    s = scores[i]
    print(l,s)