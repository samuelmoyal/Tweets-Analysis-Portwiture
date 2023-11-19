## Nom
Psychotweet

## Description
Le but du projet est d'analyser le profil social et psychologique d'un utilisteur twitter en utilisant à la fois les tweets posté par l'utilisateur et les tweets postés sur l'utilisateur.

## Visuel de l'app
Ajouer une photo de l'app

## Installation
Pour exécuter notre programme:
1. Cloner le dépot
2. Modifier le fichier `credentials.py` en ajoutant les identifiants twitter developer
3. Installer les packages suivant
```bash
pip install stop_words wordcloud pandas textblob json dash plotly express graph objects
```
4. Se placer à la racine du dépot et taper la commande suivante `python -m display.app`

## Usage
Permet de réaliser l'analyse psychologique d'un utilisateur twitter. Cette application est aussi utile pour détecter si l'environnement sur twitter d'un utilisateur est toxique ou bienveillant et elle detecte si l'utilisateur parle plutôt positivement ou négativement.

## Support
gabriel.seigneur@student-cs.fr

## Roadmap
Proposer des aides et actions pour amélirorer son environnement twitter. Par exemple une liste de musique qui correspond aux gouts de l'utilisateur. Lui afficher ses messages trop haineux pour le mettre en garde.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Je remercie toute l'équipe mercure pour ces deux superbes semaines de codingweeks !


## Project status
On avait pour projet de proposer une musique qui pourrait être bénéfique psychologiquement pour l'utilisateur de notre appli en fonction de ses préférences positives. 

## Profil psychologique de l'utilisateur

+ Son profil social (informations recueillies des tweets qui parlent de l'utilisateur)
+ Son profil psychologique (informations recueillies des statuses postés par l'utilisateur)

# Modules du package "collect"
+ Recenser les statuses où l'utilisateur apparaît sans en être l'auteur (social) 
+ Recenser les statuses publiées par l'utilisateur (psychologique) 
+ Recenser le tweet le plus populaire de l'utilisateur (en fonction de RT et de likes) (psychologique) 
+ Trouver la bio d'un utilisateur (psychologique) 
+ Conversion et stockage en .json des tweets recueillis

# Modules du package "analysis"          # Utiliser transformers
+ Nuage de mots clés pertinents utilisés par l'utilisateur (filtre à déterminer ; social & psychologique) 
+ À quel point l'utilisateur contreversé (social) (diversité des sentiments ? Viralité ?) 
+ Classification des sentiments qui décrivent le mieux comment l'utilisateur s'exprime (psychologique) (gentil / méchant=> Camembert) 
+ Classification des sentiments qui décrivent le mieux comment l'utilisateur est décrit (social) (gentil / méchant=> Camembert) 
+ Nuage de mots clés pertinents utilisés pour parler de l'utilisateur (filtrer par nature grammaticale ? noms / adj ?) 
+ Nuage des sentiments qui ressortent le plus souvent des tweets de l'utilisateur 
+ Nuage des setiments qui ressortent le plus  souvent des tweets où l'utilisateur est taggé 

# Module du package "display"
+ Camembert classification des sentimemts psychologique :
+ Camembert classification des sentimemts social + comportement final :
+ Jauge controverse :
+ Nuage de mots clés social :
+ Nuage de mots clés psychologique :
+ Évolution de l'opinion publique sur l'utilisateur au fil d'une semaine 


# Dash :
+ Changer la langue partout
+ Résoudre ce problème de padding
+ Ajouter la bio
+ Ajouter les nouvelles fonctionnalités# Samuel-Moyal-Coding-Weeks-
