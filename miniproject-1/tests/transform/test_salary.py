import pandas as pd
from src.transfom.salary import transform_salary


def test_transform_salary_range_vnd():
    df = pd.DataFrame({
        "salary": ["10 - 20 triệu"]
    })

    result = transform_salary(df)

    assert len(result) == len(df)
    assert result.loc[0, "min_salary"] == 10_000_000
    assert result.loc[0, "max_salary"] == 20_000_000
    assert result.loc[0, "salary_unit"] == "VND"


def test_transform_salary_thoa_thuan():
    df = pd.DataFrame({
        "salary": ["Thoả thuận"]
    })

    result = transform_salary(df)

    assert len(result) == len(df)
    assert result.loc[0, "min_salary"] is None
    assert result.loc[0, "max_salary"] is None
