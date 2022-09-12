
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_mantine_components as dmc


from data_etl import df_raw

dash.register_page(__name__)

layout = html.Div(children=[
    html.H3(children='Please filter and download data', style={'textAlign': 'center'}),

    dmc.Center([
        dmc.Button("Download Data", id="btn-download", style={'textAlign': 'center'}),
    ]),

    dcc.Download(id="download-dataframe-csv"),

])


@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-download", "n_clicks"),

    State(component_id='city-filter', component_property='value'),
    State(component_id='vendor-filter', component_property='value'),
    State(component_id='category-filter', component_property='value'),
    State(component_id='bottle-size-filter', component_property='value'),

    State(component_id='top-n-filter', component_property='value'),
    State(component_id='metric-chooser', component_property='value'),

    prevent_initial_call=True,
)
def download_function(
        n_clicks,
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

    return dcc.send_data_frame(df_filtered.to_csv, "mydf.csv")

