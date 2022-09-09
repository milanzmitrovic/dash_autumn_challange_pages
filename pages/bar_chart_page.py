import dash
from dash import html, dcc, callback, Input, Output

from data_etl import df_raw
from utils import bar_chart, bar_chart_grouped

dash.register_page(__name__)

layout = html.Div(
    children=[

        dcc.Graph(id='bar-chart-1'),

        dcc.Graph(id='bar-chart-2')

    ])


@callback(
    Output(component_id='bar-chart-1', component_property='figure'),
    Output(component_id='bar-chart-2', component_property='figure'),

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


    fig1 = bar_chart(
        df=df_filtered,
        x_axis='city',
        y_axis=metric,
        n_largest=n_largest

    )

    fig2 = bar_chart_grouped(
        df=df_filtered,
        x_axis='county',
        y_axis=metric,
        color='pack',
        n_largest=n_largest
    )

    return fig1, fig2

