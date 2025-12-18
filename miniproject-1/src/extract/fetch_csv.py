import logging
from io import StringIO

import requests
import pandas as pd

logger = logging.getLogger(__name__)


def fetch_csv_from_url(url: str, timeout: int = 30) -> pd.DataFrame | None:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        content = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(content))

        if df.empty:
            raise ValueError('Empty CSV file.')
        return df
    except requests.HTTPError as e:
        logger.error(f'HTTP Error when fetching {url}: {e}')
        raise
    except UnicodeDecodeError as e:
        logger.error(f'Failed to decode CSV content as utf-8: {e}')
        raise
    except pd.errors.ParserError as e:
        logger.error(f'pd failed to parse CSV: {e}')
        raise
    except Exception as e:
        logger.error(f'Error when fetching {url}: {e}')
        raise

    return None
