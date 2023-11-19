import plotly.express as px
from textblob import TextBlob
import pandas as pd
import time
from datetime import datetime, timedelta, date
from dateutil.parser import parse

# cette fonction renvoie l'opinion sur un candidat pour un jour donné


def analyse_opinion_jour(jour):
    data1 = pd.read_json("Data/statusesHashtagged.json")
    data2 = pd.read_json("Data/statusesTagged.json")
    data = pd.concat([data1, data2])
    data_small = data.loc[:, ['text', 'date']]
    data_small['date'] = pd.to_datetime(data_small['date']).dt.date
    tweets_jour = data_small.loc[data_small['date'] == jour]
    liste_text_tweet_jour = []
    for content in tweets_jour['text']:
        liste_text_tweet_jour.append(content)

    pos_tweets = []

    for tweet in liste_text_tweet_jour:
        if TextBlob(tweet).sentiment.polarity > 0:
            pos_tweets.append(tweet)

    return len(pos_tweets)*100/max(1, len(liste_text_tweet_jour))
# renvoit pourcentage positif puis neutre puis négatif


def graph_opinion_mois():  # mettre la date du jour pour le dernier jour de collect
    aujourdhui = date.today()
    jours = ['J-0', 'J-1', 'J-2']
    opinion = []
    for i in range(3):
        jour_precedent = aujourdhui - timedelta(days=i)
        opinion.append(analyse_opinion_jour(jour_precedent))
    opinion.reverse()
    fig = px.bar(x=jours, y=opinion, labels={
        'x': 'Jours', 'y': 'Opinion (en %)'})
    fig.show()


# Test
if __name__ == '__main__':
    graph_opinion_mois()
