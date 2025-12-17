import pandas as pd
from unittest.mock import patch, Mock

from src.extract.fetch_csv import fetch_csv_from_url

@patch("src.extract.fetch_csv.requests.get")
def test_fetch_csv_success(mock_get):
    csv_text = "col1,col2\n1,2\n3,4"

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = csv_text.encode("utf-8")
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    df = fetch_csv_from_url("http://fake-url")

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["col1", "col2"]
