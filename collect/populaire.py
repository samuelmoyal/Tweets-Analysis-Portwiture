import collect.collect_tweet_from_user
import json
import pandas as pd

datatest = pd.read_json("Data/tweets_written_by.json")

# Cette fonction permet de réupérer le tweet le plus populaire selon un indicateur


def tweet_populaire(data):
    compt = 0
    tweet_le_plus_pop = []
    for k in range(len(data)):
        # indicateur de populairté: somme des RT et favoris
        popu = data['retweet'][k]+data['fav'][k]
        if popu > compt:
            compt = popu
            tweet_le_plus_pop = data['text'][k]
    return tweet_le_plus_pop


# Test
if __name__ == '__main__':
    print(tweet_populaire(datatest))
