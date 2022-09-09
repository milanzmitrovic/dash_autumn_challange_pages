import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H3(children='Dash app is developed for autumn Dash challange 2022', style={'textAlign': 'center'}),

    html.H3(
        ['Developer - ',
         html.A("Milan Mitrovic", href='https://milanzmitrovic.github.io')
         ],
        style={'textAlign': 'center'}),



])

