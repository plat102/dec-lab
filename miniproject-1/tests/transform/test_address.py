import pandas as pd
from src.transfom.address import transform_address


def test_transform_address_city_only():
    df = pd.DataFrame({
        "address": ["Hà Nội"]
    })

    result = transform_address(df)

    assert len(result) == len(df)
    assert result.loc[0, "city"] == "Hà Nội"
    assert result.loc[0, "district"] is None


def test_transform_address_city_district():
    df = pd.DataFrame({
        "address": ["Hồ Chí Minh: Quận 1: Hà Nội: Cầu Giấy"]
    })

    result = transform_address(df)

    assert len(result) == len(df)
    assert result.loc[0, "city"] == "Hồ Chí Minh"
    assert result.loc[0, "district"] == "Quận 1"

def test_transform_address_special_location():
    df = pd.DataFrame({
        "address": ["Toàn Quốc"]
    })

    result = transform_address(df)

    assert len(result) == len(df)
    assert result.loc[0, "city"] == "Toàn Quốc"
    assert result.loc[0, "district"] is None
