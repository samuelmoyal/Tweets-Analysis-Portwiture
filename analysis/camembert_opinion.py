
import seaborn as sns
from analysis.analyse_positivite import polarity
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go


def camembertopinion():
    data=pd.read_json("Data/tweets_written_by.json")
    values=[polarity(data)[0],polarity(data)[1],polarity(data)[2]]
    labels = ['Négativité', 'Neutralité', 'Positivité']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    return(fig)

    


#test
if __name__ == '__main__':
    camembertopinion().show()
