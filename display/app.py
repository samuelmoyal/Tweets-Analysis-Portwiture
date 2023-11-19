# Imports

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

import analysis.camembert2 as cam2
import analysis.camembert_opinion as camo
import analysis.evolution_opinion_temps as eot
import display.diagramme_like as dial


# Import analysis modules
import analysis.nuage_keywords as kws
import analysis.wcloud_about_user as kwp
import collect.collect_tweet_from_user as cfu
# Import collect modules
import collect.collect_statuses_where as csw

'''
Ce module contient les instructions pour initialiser l'application Dash. Il est formé de 2 parties :
- Le layout (on crée la structure et le contenu de l'application web)
- Le Callback (on définit ce qui s'exécute (via une fonction update_app) pour update l'application après que l'utilisateur
    ait saisi le nom d'un compte Twitter à analyser)

Pour lancer l'application, saisir dans le terminal la commande 'py -m display.app' ou 'python -m display.app' ou 'python3 -m display.app'
'''

# dico couleurs
colour = {'social_div': '#FFBEBE', 'psy_div': '#C4FCFC'}

# Initialisation des variables
donut_social = []
donut_psy = []
diagramme_follower = []
# Création de l'application dash
app = Dash(__name__)
# ------------------------------------------------------------------------------
# App layout
'''
On liste ici les children du layout. Dans l'ordre :
- Titre de l'application (H1)
- Division de l'input (saisir le nom du compte Twitter à analyser)
- Fonctionnalités :
    - Nuage de mots
    - Donut
    - 
'''

app.layout = html.Div(children=[

    html.H1(children="PsychoTweet", style={
            'text-align': 'center', 'font-family': 'Monaco'}),


    # J'ajoute ici l'input où l'utilisateur entrera le nom du compte Twitter à analyser
    html.Div(id='input_header',

             children=[
                 # Titre au-dessus de l'input
                 html.H2(children='Choisissez un compte Twitter à analyser', style={
                         'font-family': 'Monaco'}),
                 # Fenêtre de l'input
                 dcc.Input(id="input_twitterUsername",
                           placeholder="Saisissez le nom d'un compte Twitter...",
                           type='text',
                           value='',
                           debounce=True
                           )

             ]),

    html.Div(id='output_container', children=[]),
    html.Br(),

    # Portrait social
    html.Div(id='portrait_social', style={'text-align': 'center', 'background-color': colour['social_div'],
                                          'width': '600px', 'height':'1500px', 'float':'left'}, children=[

        # Titre de la section
        html.H1(children='Portrait social', style={'font-family': 'Monaco'}),

        # Nuage de mots
        html.Div(children=[
            # Titre du nuage de mots
            html.H3(children="Nuage de mots utilisés dans les tweets pour décrire l'utilisateur", style={
                'text-align': 'center'}),

            # Nuage de mots : on exécute la fonction qui plot le WordCloud direct
            html.Img(id='wordcloud_social', src='assets/wordcloud_social.png', style={'height': '450px', 'width': '550px',
                                                                                      'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '2px', 'margin-bottom': '2px', 'padding': '2px 2px'})
        ], title="Nuage de mots utilisés dans les tweets pour décrire l'utilisateur"

        ),

        # Donut
        html.Div(children=[
            html.H3(children="Avis exprimés sur l'utilisateur",
                    style={'text-align': 'center'}),
            dcc.Graph(id='donut_social', style={
                      'height': '300px', 'width': '550px', 'margin-left': 'auto', 'margin-right': 'auto'})
        ]),

        # Graphe évolution opinion = f(temps)
        html.Div(children=[
            html.H3(children="Evolution de l'opinion positive sur les 3 derniers jours", style={
                    'text-align': 'center'}),
            dcc.Graph(id='graph_opinion', style={
                      'height': '300px', 'width': '550px', 'margin-left': 'auto', 'margin-right': 'auto'})
        ])
    ]),
        
    # Portrait psychologique
    html.Div(id='portrait_psy', style={'text-align': 'center', 'background-color': colour['psy_div'],
                                       'width': '600px', 'height':'1500px', 'float':'right'}, children=[

        # Titre de la section
        html.H1(children='Portrait psychologique',
                style={'font-family': 'monaco'}),

        # Nuage de mots
        html.Div(children=[
            # Titre du nuage de mots
            html.H3(children="Nuage des mots utilisés par l'utilisateurs dans ses tweets", style={
                'text-align': 'center'}),

            # Nuage de mots
            html.Img(id='wordcloud_psycho', src='assets/wordcloud_psycho.png', style={'height': '450px', 'width': '550px',
                                                                                      'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '2px', 'margin-bottom': '2px', 'padding': '2px 2px'})
        ], title="Nuage des mots utilisés par l'utilisateurs dans ses tweets"),

        # Donut
        html.Div(children=[
            html.H3(children="Sentiments exprimés par l'utilisateur",
                    style={'text-align': 'center'}),
            dcc.Graph(id='donut_psy', style={
                'height': '300px', 'width': '550px', 'margin-left': 'auto', 'margin-right': 'auto'})
        ]),
        
        # Diagramme followers
        html.Div(children=[ 
            html.H3(children=[],
                    style={'text-align': 'center'}),          
            dcc.Graph(id='diagramme_follower',style={
                'height': '300px', 'width': '550px', 'margin-left': 'auto', 'margin-right': 'auto'})
        ])
    ]),
])


# ------------------------------------------------------------------------------
'''
On relie les dash components (dcc), les propriétés de certains objets html avec l'input via le callback
(bloc de fonctions qui s'exécute dès que l'input est modifié par l'utilisateur)
'''


@app.callback(
    # On liste les outputs de l'application
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='wordcloud_social', component_property='src'),
     Output(component_id='wordcloud_psycho', component_property='src'),
     Output(component_id='donut_social', component_property='figure'),
     Output(component_id='donut_psy', component_property='figure'),
     Output(component_id='graph_opinion', component_property='figure'),
     Output(component_id='diagramme_follower', component_property='figure'),
     Output(component_id='statut',component_property='children')]
     

    # On prend en input de l'app Dash le username entré par l'utilisateur
    Input(component_id='input_twitterUsername', component_property='value')
)
def update_app(username_selected):
    print(username_selected)
    print(type(username_selected))

    container = f"L'utilisateur choisi est : {username_selected}"

    # On run ici les fonctions de collect

    csw.collectStatusesHashtagged(username_selected)
    csw.collectStatusesTagged(username_selected)
    cfu.collect_by_user(username_selected)

    # On run les fonctions d'analyse
    kws.plotWordCloudKeyWords()
    kwp.makewCloud()
    donut_social = cam2.camembert2()
    donut_psy = camo.camembertopinion()
    graph_opinion = eot.graph_opinion_mois()
    diagramme_follower = dial.diagramme_follower()

    return container, 'assets/wordcloud_social.png', 'assets/wordcloud_psycho.png', donut_social, donut_psy, graph_opinion, diagramme_follower, statut


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
