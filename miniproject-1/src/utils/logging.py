import logging
import os
from datetime import datetime


def setup_pipeline_logging():
    log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f'elt_{datetime.now().strftime("%Y%m%d-%H%M%S")}.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        force=True
    )
