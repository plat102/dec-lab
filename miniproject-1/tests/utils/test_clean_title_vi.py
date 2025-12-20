from src.utils.helpers import clean_title_vi


def test_clean_title_basic():
    title = "Senior Data Engineer"
    assert clean_title_vi(title) == "data engineer"


def test_clean_title_remove_accent():
    title = "Kỹ sư dữ liệu"
    assert clean_title_vi(title) == "ky su du lieu"

def test_clean_title_not_string():
    assert clean_title_vi(2025) == ""

def test_clean_title_empty():
    assert clean_title_vi("") == ""
