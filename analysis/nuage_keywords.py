import os
from wordcloud import WordCloud
from textblob import TextBlob
from stop_words import get_stop_words
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# Nettoie le contenu d'un tweet, renvoie une liste de strings
def cleanTweet(text):
    #specialCharacters = {'\u00e0':'a', '\u00e2':'a', '\u00e4':'a', '\u00e6':'ae', '\u00e7':'c', '\u00e8': 'e', '\u00e9': 'e', '\u00ea': 'e', '\u00eb': 'e', '\u00ee': 'i', '\u00f9':'u', '\u00fa': 'u', '\u00fb': 'u', '\u00f4': 'o'}
    spen = set(get_stop_words('english'))
    spfr = set(get_stop_words('french'))
    res = []
    # on enlève les erreurs dûes aux caractères spéciaux avec les codes unicode
    # for spCharKey in specialCharacters.keys():
    #text.replace(spCharKey, specialCharacters[spCharKey])
    blob = TextBlob(text)
    shitCharacters = {';', ':', '.', ' ', '&', 'RT', '@', '#'}
    for word in blob.words:
        # On enlève les stopwords
        if (word not in spen) and (word not in spfr):
            # On enlève les mots qui sont de la ponctuation ou qui commencent par une majuscule (noms propres)
            if word not in shitCharacters and not (word[0].isupper()):
                # Un test supplémentaire pour dégager les caractères récurrents dans les tweets
                if ('@' not in word) and ('#' not in word) and ('_' not in word) and ('.' not in word):
                    res.append(word)
    return res


def getFrequencyDictForText(text):
    freqDict = {}

    # making dict for counting frequencies

    words = cleanTweet(text)
    for i in range(len(words)):
        word = words[i]
        # On ajoute seulement les mots 'lemmatized' dans freqDict
        freq = freqDict.get(word.lemmatize(), 0)
        freqDict[words[i].lemmatize()] = freq + 1
    return freqDict

# def defineColour(text):
    # si le mot est positif, il est bleu, s'il est négatif, il est rouge, s'il est neutre, il est jaune


def makeImage(text):
    #img = np.array(Image.open("tweet_analysis/Logo3"))

    wc = WordCloud(background_color="white",
                   max_words=1000)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    if os.path.isfile('display/assets/wordcloud_social.png'):
        os.remove('display/assets/wordcloud_social.png')
    plt.savefig('display/assets/wordcloud_social.png', transparent=True)


def plotWordCloudKeyWords():
    data1 = pd.read_json("Data/statusesHashtagged.json")
    data2 = pd.read_json("Data/statusesTagged.json")
    data = pd.concat([data1, data2])
    wholeFreqDict = {}
    plt.savefig('display/assets/wordcloud_social.png', transparent=True)
    for tweet in data['text']:
        wholeFreqDict.update(getFrequencyDictForText(tweet))
    makeImage(wholeFreqDict)


if __name__ == '__main__':
    plotWordCloudKeyWords()

    #Test si dataframe vide
    import collect.collectStatusesWhere  as csw
    csw.collectStatusesHashtagged('')
    csw.collectStatusesTagged('')
    plotWordCloudKeyWords()
