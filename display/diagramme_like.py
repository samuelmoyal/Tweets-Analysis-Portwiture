import seaborn as sns
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

def diagramme_follower():
    data=pd.read_json("Data/Userinfo.json")
    # assume you have a "long-form" data frame
    df = pd.DataFrame({
    "Popularité": ["Nombre d'abonné","Nombre d'abonnement"],
    "Amount": [data["followercount"][0],data["friendscount"][0]]})
    fig = px.bar(df, x="Popularité", y="Amount", barmode="group")
    return fig

# test
if __name__ == '__main__':
    diagramme_follower().show()





