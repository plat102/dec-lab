import pandas as pd
from src.utils.helpers import parse_address


def test_parse_address_full():
    value = "Hà Nội: Thanh Xuân: Hải Dương: TP Hải Dương"
    result = parse_address(value)

    assert result == [{"city": "Hà Nội", "district": "Thanh Xuân"},
                      {"city": "Hải Dương", "district": "TP Hải Dương"}]


def test_parse_address_only_city():
    value = "Hồ Chí Minh"
    result = parse_address(value)

    assert result == [{"city": "Hồ Chí Minh"}]


def test_parse_address_special_location():
    value = "Toàn Quốc"
    result = parse_address(value)

    assert result == [{"city": "Toàn Quốc"}]


def test_parse_address_none():
    result = parse_address(None)
    assert result == {"city": None, "district": None}


def test_parse_address_na():
    result = parse_address(pd.NA)
    assert result == {"city": None, "district": None}
