import pytest
import pandas as pd

@pytest.fixture
def empty_df():
    return pd.DataFrame()
