from src.utils.helpers import classify_job_group


def test_classify_backend():
    title = "Senior Backend Engineer"
    assert classify_job_group(title) == "backend"

def test_classify_data():
    title = "Data Engineer"
    assert classify_job_group(title) == "data"

def test_classify_unknown():
    title = "Office Assistant"
    assert classify_job_group(title) == "other"
