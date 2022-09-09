
import pandas as pd

df_raw = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv',
    date_parser='date'

)

df_raw['date'] = pd.to_datetime(df_raw['date'])


