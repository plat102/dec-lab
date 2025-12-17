import pandas as pd

from src.utils.helpers import classify_job_group


def transform_job_title(df: pd.DataFrame) -> pd.DataFrame:
    df['job_group'] = df['job_title'].apply(classify_job_group)
    df[['job_group', 'job_title']].sample(n=20)
    return df
