
import io
import requests
import pandas as pd


def fetch_csv_from_url(url: str, timeout: int = 30) -> pd.DataFrame:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    return pd.read_csv(io.StringIO(response.content.decode('utf-8')))
