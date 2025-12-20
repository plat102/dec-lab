import pytest
from src.utils.helpers import extract_salary_info


@pytest.mark.parametrize(
    "raw, expected",
    [
        (
            "10 - 20 triệu",
            {"num": 15, "min": 10, "max": 20, "unit": "VND"},
        ),
        (
            "Trên 15 triệu",
            {"num": 15, "min": 15, "max": None, "unit": "VND"},
        ),
        (
            "Tới 30 triệu",
            {"num": 30, "min": None, "max": 30, "unit": "VND"},
        ),
        (
            "2000 USD",
            {"num": 2000, "min": 2000, "max": 2000, "unit": "USD"},
        ),
        (
            "Thoả thuận",
            {"num": None, "min": None, "max": None, "unit": "VND"},
        ),
        (
            None,
            {"num": None, "min": None, "max": None, "unit": None},
        ),
    ],
)
def test_extract_salary_info(raw, expected):
    result = extract_salary_info(raw)

    for k, v in expected.items():
        assert result[k] == v
