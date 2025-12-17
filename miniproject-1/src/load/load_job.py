
import pandas as pd
from src.load.postgres import create_pg_engine, load_dataframe_to_sql

def load_jobs_to_postgres(df: pd.DataFrame):

    engine = create_pg_engine()
    load_dataframe_to_sql(df=df,
                          engine=engine,
                          table_name="jobs",
                          if_exists="replace")
