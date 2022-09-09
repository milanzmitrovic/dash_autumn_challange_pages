import dash
from dash import html, dcc, Input, Output, callback
import plotly.express as px

from data_etl import df_raw
from utils import line_chart

dash.register_page(__name__)

layout = html.Div(
    children=[
        dcc.Graph(id='line-chart')
    ])


@callback(
    Output(component_id='line-chart', component_property='figure'),

    Input(component_id='city-filter', component_property='value'),
    Input(component_id='vendor-filter', component_property='value'),
    Input(component_id='category-filter', component_property='value'),
    Input(component_id='bottle-size-filter', component_property='value'),

    Input(component_id='top-n-filter', component_property='value'),
    Input(component_id='metric-chooser', component_property='value'),

)
def update_bar_charts(
        city,
        vendor_name,
        category_name,
        bottle_volume,
        n_largest,
        metric
):

    df_filtered = df_raw.copy()

    if not city:
        print('Filter city is empty')
    else:
        df_filtered = df_filtered.query("city == @city")

    if not category_name:
        print('Filter category_name is empty')
    else:
        df_filtered = df_filtered.query("category_name == @category_name")

    if not vendor_name:
        print('Filter vendor_name is empty')
    else:
        df_filtered = df_filtered.query("vendor_name == @vendor_name")

    if not bottle_volume:
        print('Filter bottle_volume is empty')
    else:
        bottle_volume = int(bottle_volume)
        df_filtered = df_filtered.query("bottle_volume_ml == @bottle_volume")

    fig1 = line_chart(
        df=df_filtered,
        x_axis='date',
        y_axis=metric
    )

    return fig1






