import pandas as pd

from src.utils.helpers import parse_address

def transform_address(df: pd.DataFrame) -> pd.DataFrame:
    df['address_info'] = df['address'].apply(lambda x: parse_address(x))

    # Get first address city & district info into
    df['city'] = df['address_info'].apply(lambda x: x[0].get('city'))
    df['district'] = df['address_info'].apply(lambda x: x[0].get('district'))

    return df
