import logging
import os

from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
import pandas as pd

logger = logging.getLogger(__name__)

# Load from .env file
load_dotenv()


def create_pg_engine() -> Engine:
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")
    database = os.getenv("PG_DATABASE")

    url = f"postgresql://{user}:{password}@{host}/{database}"
    engine = create_engine(url)

    return engine


def load_dataframe_to_sql(df: pd.DataFrame, engine: Engine, table_name: str, if_exists: str = 'append') -> None:
    logger.info(f"Loading {len(df)} rows into table {table_name}")

    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)  # type: ignore[arg-type]

    logger.info(f"Done loading into table {table_name}")
