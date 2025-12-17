import logging
from src.pipeline.run_etl import run_etl

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    run_etl()
