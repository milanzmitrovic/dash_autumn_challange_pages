from dash import Dash, html, dcc, callback, Input, Output, State
import dash
import pandas as pd
import dash_mantine_components as dmc
from data_etl import df_raw
from utils import (
    create_metric_chooser,
    create_top_n_filter,
    create_city_filter,
    create_category_filter,
    create_vendor_filter,
    create_bottly_volume_filter,
    create_simple_grid,
)

app = Dash(__name__, use_pages=True)

sidebar = dmc.Navbar(
    fixed=True,
    style={"marginLeft": 25},
    width={"base": 300},
    height=300,
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type="scroll",
            children=[
                dmc.Group(
                    direction="column",
                    children=[
                        dmc.Button("Filters", id="modal-demo-button"),
                        dmc.Modal(
                            size="lg",
                            title="Dataset Filters",
                            id="modal",
                            children=create_simple_grid(
                                component_list=[
                                    create_metric_chooser(),
                                    create_top_n_filter(),
                                    create_city_filter(),
                                    create_category_filter(),
                                    create_vendor_filter(),
                                    create_bottly_volume_filter(),
                                ]
                            ),
                        ),
                    ],
                ),
                dmc.Divider(style={"marginBottom": 20, "marginTop": 20}),
                dmc.Group(
                    direction="column",
                    children=[
                        dcc.Link(
                            dmc.Text(page["name"], size="sm", color="gray"),
                            href=page["path"],
                            id=page["name"],
                            style={"textDecoration": "none"},
                        )
                        for page in dash.page_registry.values()
                    ],
                ),
            ],
        )
    ],
)


app.layout = dmc.Container(
    [
        dmc.Header(
            height=40,
            children=[html.H1("Dash Autumn Challange", style={"textAlign": "center"})],
            style={"backgroundColor": "#FFFFFF"},
        ),
        sidebar,
        dmc.Container(
            dash.page_container,
            size="lg",
            pt=20,
            style={"marginLeft": 350},
        ),
    ],
    fluid=True,
)


@callback(
    Output("modal", "opened"),
    Input("modal-demo-button", "n_clicks"),
    State("modal", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


if __name__ == "__main__":
    app.run_server(debug=True)