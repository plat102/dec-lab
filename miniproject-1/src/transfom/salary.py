
import pandas as pd
from src.utils.helpers import extract_salary_info


def transform_salary(df: pd.DataFrame) -> pd.DataFrame:
    df['salary_info'] = df['salary'].apply(extract_salary_info)
    df['salary_num'] = df['salary_info'].apply(lambda x: x.get('num') * (10 ** 6)
    if (x.get('num') and 'VND' in x.get('unit')) else None)
    df['min_salary'] = df['salary_info'].apply(
        lambda x: x.get('min') * (10 ** 6) if x.get('min') and x.get('unit') == 'VND' else x.get('min'))
    df['max_salary'] = df['salary_info'].apply(
        lambda x: x.get('max') * (10 ** 6) if x.get('max') and x.get('unit') == 'VND' else x.get('max'))
    df['salary_unit'] = df['salary_info'].apply(lambda x: x.get('unit'))

    df.drop(columns=['salary_info'], inplace=True)

    return df
