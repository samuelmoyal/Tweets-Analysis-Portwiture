import dash_bootstrap_components as dbc
from dash import html

html.Div(html.H6(
    id='output-1',
    children=[
        'This is integer ',
        html.Span(id='output-2', children=''),
    ]
))
