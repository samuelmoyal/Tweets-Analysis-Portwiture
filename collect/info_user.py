import tweepy

from collect.credentials import *
from collect.twitter_connection_setup import twitter_setup

import json

# Cette fonction renvoie plusieurs informations relatives à un utilisateur


def collectuser(userid):
    connexion = twitter_setup()
    user = connexion.get_user(screen_name=userid)
    data = {'id': user.id, 'name': user.name, 'pseudo': user.screen_name, 'bio': user.description,
            'followercount': user.followers_count, 'friendscount': user.friends_count, 'photodeprofil': user.profile_image_url_https, 'image':user.profile_banner_url}
    with open("Data/Userinfo.json", "w+") as write_file:
        json.dump(data, write_file)


if __name__ == '__main__':
    print(collectuser('EmmanuelMacron'))
