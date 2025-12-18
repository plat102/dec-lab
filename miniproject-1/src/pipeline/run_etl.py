import logging

import pandas as pd

from config.job_data import DATA_URL
from src.extract.fetch_csv import fetch_csv_from_url
from src.transfom.salary import transform_salary
from src.transfom.address import transform_address
from src.transfom.job_title import transform_job_title
from src.load.load_job import load_jobs_to_postgres

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_etl():
    logger.info('Running ETL')

    # ---------- EXTRACT ----------
    df_raw = fetch_csv_from_url(DATA_URL)

    # ---------- TRANSFORM ----------
    logger.info(' - Transforming salary...')
    df = transform_salary(df_raw)
    logger.info(' - Transforming address...')
    df = transform_address(df)
    logger.info(' - Transforming job title...')
    df = transform_job_title(df)

    df['processed_time'] = pd.Timestamp.now()

    # ---------- LOAD ----------
    # print(df.head())
    logger.info(' - Saving transformed data...')

    load_jobs_to_postgres(df)

    print("\n" + "=" * 50)
    print("ETL Pipeline Complete!")

    return df


if __name__ == "__main__":
    df = run_etl()

    # Display sample results
    print("\nSample results:")
    print(df[['job_title', 'job_group', 'salary', 'min_salary', 'max_salary', 'city']].head(10))

