import pandas as pd
from textblob import TextBlob

datatest=pd.read_json("Data/tweets_written_by.json")


def polarity(data):
    twt=data["text"]
    l=len(twt)
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []
    for state in twt:
        if TextBlob(state).sentiment.polarity > 0.3:
            pos_tweets.append(state)
        elif TextBlob(state).sentiment.polarity > -0.3:
            neu_tweets.append(state)
        else:
            neg_tweets.append(state)
    return (len(pos_tweets)*100/l,len(neu_tweets)*100/l,len(neg_tweets)*100/l)
    

#test:
if __name__=='__main__':
    print(polarity(datatest))


