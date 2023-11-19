import json
from collect_tweet_from_user import collect_by_user
from textblob import TextBlob


def obj_ou_subj(user_id):
    liste = collect_by_user(user_id)
    moy = 0
    for tweet in liste:
        moy += TextBlob(tweet['text']).sentiment.subjectivity
    return moy/len(liste)


print(obj_ou_subj(''))
