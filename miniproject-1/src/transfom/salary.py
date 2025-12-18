import pandas as pd
from src.utils.helpers import extract_salary_info
from src.utils.utils import convert_unit_to_vnd


def transform_salary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise pd.errors.EmptyDataError
    elif 'salary' not in df.columns:
        raise ValueError('Missing required column "salary"')

    df['salary_info'] = df['salary'].apply(extract_salary_info)
    df['salary_num'] = df['salary_info'].apply(lambda x: convert_unit_to_vnd(x.get('num'), x.get('unit')))
    df['min_salary'] = df['salary_info'].apply(lambda x: convert_unit_to_vnd(x.get('min'), x.get('unit')))
    df['max_salary'] = df['salary_info'].apply(lambda x: convert_unit_to_vnd(x.get('max'), x.get('unit')))
    df['salary_unit'] = df['salary_info'].apply(lambda x: x.get('unit'))

    df.drop(columns=['salary_info'], inplace=True)

    return df
