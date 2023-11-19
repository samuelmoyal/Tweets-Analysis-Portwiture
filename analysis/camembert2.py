import matplotlib.pyplot as plt
import seaborn as sns
from analysis.analyse_opinion import polarity2
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go


def camembert2():
    d1 = pd.read_json("Data/statusesHashtagged.json")
    d2 = pd.read_json("Data/statusesTagged.json")
    data = pd.concat([d1, d2])
    labels = ['Négativité', 'Neutralité', 'Positivité']
    values = [polarity2(data)[0], polarity2(data)[1], polarity2(data)[2]]

    # Use hole to create a donut-like pie chart

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    return (fig)


# test
if __name__ == '__main__':
    camembert2().show()
