from collect.credentials import *
from collect.twitter_connection_setup import twitter_setup
import json
import tweepy


def collectStatusesTagged(user):
    # On traite le cas zéro
    if len(user) == 0:
        with open("Data/statusesTagged.json", "w+") as write_file:
            json.dump([], write_file)
        return
    connexion = twitter_setup()
    tweets = connexion.search_30_day('CWSearch30Days', query=f"@{user}")
    res = []
    for tweet in tweets:
        res.append({'id': tweet.id, 'text': tweet.text, 'date': tweet.created_at})
    # On crée ou overwrite un fichier dans Data avec une liste de dicos
    with open("Data/statusesTagged.json", "w+") as write_file:
        json.dump(res, write_file, default=str)


def collectStatusesHashtagged(user):
    # On traite le cas zéro
    if len(user) == 0:
        with open("Data/statusesTagged.json", "w+") as write_file:
            json.dump([], write_file)
        return
    connexion = twitter_setup()
    tweets = connexion.search_30_day('CWSearch30Days', query=f"#{user}")
    res = []
    for tweet in tweets:
        res.append({'id': tweet.id, 'text': tweet.text, 'date': tweet.created_at})
    # On crée ou overwrite un fichier dans Data avec une liste de dicos
    with open("Data/statusesHashtagged.json", "w+") as write_file:
        json.dump(res, write_file, default=str)


if __name__ == '__main__':
    collectStatusesHashtagged('Macron')
    collectStatusesTagged('Macron')
