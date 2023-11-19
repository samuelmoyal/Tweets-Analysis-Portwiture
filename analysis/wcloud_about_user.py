from textblob import TextBlob as tb
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stop_words import get_stop_words
import os

# le but de cette fonctionnalité est de créer un wordcloud fréquentiel en fonction des tweets de l'utilisateur


def strAboutUser():  # On crée d'abord une liste des mots de l'ensemblme des tweets sous leur forme de racine
    hastuser = pd.read_json("Data/tweets_written_by.json")
    res = []
    spen = set(get_stop_words('english'))

    spfr = set(get_stop_words('french'))
    for t in hastuser["text"]:
        sentence = tb(t)
        words = sentence.words.lower()
        for i in words:
            if i not in spen and i not in spfr:
                res.append(i.lemmatize())
    return res


def frequence(r):  # On détermine ensuite la fréquence des mots

    d = {}
    for w in r:
        if w in d.keys() and w not in ["http", "rt"] and len(w) != 1:
            d[w] += 1
        else:
            d[w] = 1

    return d


def makewCloud():  # Enfin on utilkise Wordcloud pour créer l'image souhaitée
    texte = strAboutUser()
    wc = WordCloud(background_color="white", max_words=100)
    # generate word cloud
    wc.generate_from_frequencies(frequence(texte))

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    if os.path.isfile('display/assets/wordcloud_psycho.png'):
        os.remove('display/assets/wordcloud_psycho.png')
    plt.savefig('display/assets/wordcloud_psycho.png', transparent=True)


if __name__ == '__main__':
    makewCloud()
