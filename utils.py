import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd

from data_etl import df_raw


def bar_chart(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        n_largest=10
):
    # Aggregating data before plotting
    dff = df[[
        x_axis,
        y_axis
    ]].groupby(
        by=[x_axis],
        as_index=False
    ).agg('sum')

    dff = dff.nlargest(n=n_largest, columns=y_axis)

    dff.sort_values(by=y_axis, inplace=True, ascending=False)

    # Creating figure
    fig = px.histogram(
        dff,
        x=x_axis,
        y=y_axis,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title=y_axis,
        xaxis_title=x_axis
    )
    return fig


def bar_chart_grouped(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        color: str,
        barmode: str = 'group',
        n_largest=10
):
    # Aggregating data before plotting
    dff = df[[
        x_axis, y_axis, color
    ]].groupby(
        by=[x_axis, color],
        as_index=False
    ).sum()

    dff = dff.nlargest(n=n_largest, columns=y_axis)

    # Creating figure
    fig = px.histogram(
        dff,
        x=x_axis,
        y=y_axis,
        color=color,
        barmode=barmode,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title=y_axis,
        xaxis_title=x_axis
    )
    return fig


def create_metric_chooser():
    return dmc.Select(
        label="Select Metric",
        placeholder="Please select metric",
        id='metric-chooser',
        value='volume_sold_gallons',
        data=[
            'volume_sold_gallons',
            'volume_sold_liters',
            'sale_dollars',
            'bottles_sold',
            'state_bottle_retail',
            'state_bottle_cost',
            'bottle_volume_ml',
            'pack'],
        style={"width": 200, "marginBottom": 10},
    )


def create_top_n_filter():
    return dmc.NumberInput(
        label="Top N ",
        value=5,
        min=1,
        step=1,
        max=100,
        style={"width": 200},
        id='top-n-filter'
    )


def create_city_filter():
    return dmc.Select(
        label="City",
        placeholder="Select one",
        id="city-filter",
        clearable=True,
        data=df_raw['city'].unique().astype(str).tolist(),
        style={"width": 200, "marginBottom": 10},
    )


def create_category_filter():
    return dmc.Select(
        label="Category",
        placeholder="Select one",
        id="category-filter",
        clearable=True,
        data=df_raw['category_name'].unique().astype(str).tolist(),
        style={"width": 200, "marginBottom": 10},
    )


def create_vendor_filter():
    return dmc.Select(
        label="Vendor",
        placeholder="Select one",
        id="vendor-filter",
        clearable=True,
        data=df_raw['vendor_name'].unique().astype(str).tolist(),
        style={"width": 200, "marginBottom": 10},
    )


def create_bottly_volume_filter():
    return dmc.Select(
        label="Bottle volume ml",
        placeholder="Select one",
        id="bottle-size-filter",
        clearable=True,
        data=df_raw['bottle_volume_ml'].unique().astype(str).tolist(),
        style={"width": 200, "marginBottom": 10},
    )


def create_simple_grid(component_list: list):
    return dmc.Container([
        dmc.SimpleGrid(
            spacing='lg',
            cols=2,
            breakpoints=[
                {"maxWidth": 980, "cols": 3, "spacing": "md"},
                {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                {"maxWidth": 600, "cols": 1, "spacing": "sm"},
            ],

            style={
                "textAlign": "center",
            },

            children=component_list)
    ])


def line_chart(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        color: str = None
):

    dff = df.sort_values(by=x_axis)

    fig = px.line(
        data_frame=dff,
        x=x_axis,
        y=y_axis,
        color=color,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title='Price',
        xaxis_title='Date'
    )

    return fig



