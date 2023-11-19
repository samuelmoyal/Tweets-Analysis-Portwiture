import pandas as pd
from textblob import TextBlob

d1=pd.read_json("Data/statusesHashtagged.json")
d2=pd.read_json("Data/statusesTagged.json")
datatest=pd.concat([d1,d2])


def polarity2(data):
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
    

#test
if __name__=='__main__':
    print (polarity2(datatest))
