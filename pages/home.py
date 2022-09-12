import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    dcc.Markdown('''
        ### Dash app is developed for the [Plotly Autumn Challenge 2022](https://community.plotly.com/t/autumn-community-app-challenge/66996)
    ''', link_target='_blank'),

    html.H3(
        ['Developer - ',
         html.A("Milan Mitrovic", href='https://milanzmitrovic.github.io', target='_blank')
        ])

], style={'textAlign': 'center'})

