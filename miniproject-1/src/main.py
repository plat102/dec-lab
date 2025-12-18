import logging
from src.pipeline.run_etl import run_etl

def main():
    logging.basicConfig(level=logging.INFO)
    run_etl()

if __name__ == '__main__':

    main()
