import logging
import os

from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

import pandas as pd

logger = logging.getLogger(__name__)

# Load from .env file
load_dotenv()

def create_pg_engine() -> Engine:
    required_env_vars = ['PG_HOST', 'PG_PORT', 'PG_USER', 'PG_PASSWORD', 'PG_DATABASE']
    check_env = [v for v in required_env_vars if not os.getenv(v)]
    if len(check_env) > 0:
        raise RuntimeError(f"Missing required environment variables: {check_env}")

    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")
    database = os.getenv("PG_DATABASE")

    url = f"postgresql://{user}:{password}@{host}/{database}"
    engine = create_engine(url, pool_pre_ping=True)

    return engine


def load_dataframe_to_sql(
    df: pd.DataFrame,
    engine: Engine,
    table_name: str,
    if_exists: str = 'append',
    chunksize: int = 500) -> None:

    if df.empty:
        logger.warning(f'DataFrame is empty, skipping loading into table {table_name}')
        return

    logger.info(f"Loading {len(df)} rows into table {table_name}")
    try:
        df.to_sql(table_name, con=engine, if_exists=if_exists, index=False,chunksize=chunksize)  # type: ignore[arg-type]
    except SQLAlchemyError as e:
        logger.error(f"Database error when loading data.")
        logger.error(e)
        raise e
    except Exception as e:
        logger.error(f"Unexpected exception when loading data.")
        raise
    logger.info(f"Done loading into table {table_name}")
