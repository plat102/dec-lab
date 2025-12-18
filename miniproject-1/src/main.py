import logging
from src.pipeline.run_etl import run_etl
from src.utils.logging import setup_pipeline_logging

def main():
    setup_pipeline_logging()
    logger = logging.getLogger(__name__)

    logger.info('\n Starting ETL job')
    try:
        run_etl()
        logger.info('\n Finished ETL job')
    except Exception as e:
        logger.exception(f'ETL job failed: {e}')
        raise

if __name__ == '__main__':
    main()
