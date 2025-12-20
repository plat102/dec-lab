import pandas as pd
from src.transfom.job_title import transform_job_title

def test_transform_job_title_grouping():
    df = pd.DataFrame({
        "job_title": [
            "Data Analytics Engineer",
            "Lập Trình Viên Backend",
            "Kế Toán Tổng Hợp"
        ]
    })

    out = transform_job_title(df)

    assert len(out) == len(df)
    assert out.loc[0, "job_group"] == "data"
    assert out.loc[1, "job_group"] == "backend"
    assert out.loc[2, "job_group"] == "other"
