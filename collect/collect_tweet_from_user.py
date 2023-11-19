# renvoie 100 tweets écris par un utilisateur donné
import collect.twitter_connection_setup as connect
import json
from dateutil.parser import parse
import time


def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id=user_id, count=100)
    liste = []
    for tweet in statuses:
        liste.append({'id': tweet.id, 'text': tweet.text,
                     'retweet': tweet.retweet_count, 'fav': tweet.favorite_count})

    with open("Data/tweets_written_by.json", "w+") as write_file:
        json.dump(liste, write_file)


# test avec macron
if __name__ == '__main__':
    collect_by_user(1976143068)
