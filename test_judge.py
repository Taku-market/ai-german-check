import pytest
from judge import parse_answer, judge_job

@pytest.mark.parametrize("text, expected",[
    ('{"requires_german": true}', True),
    ('{"requires_german": false}', False),
    ('Yes, German is required.', None),
    ('', None),
    ('{"answer": true}', None),
])
def test_parse_answer(text, expected):
    assert parse_answer(text) == expected

def fake_true(description):
    return '{"requires_german": true}'

def fake_false(description):
    return '{"requires_german": false}'

def fake_broken(description):
    return 'Sorry, I found the position that suits you.'

def test_judge_job_true():
    assert judge_job("We are seeking someone good at this industry", fake_true) == True

def test_judge_job_false():
    assert judge_job("We are seeking someone good at this industry", fake_false) == False

def test_judge_job_fake_broken():
    assert judge_job("We are seeking someone good at this industry", fake_broken) == None

def fake_error(description):
    raise ConnectionError("network is down")

def test_judge_job_api_error():
    with pytest.raises(ConnectionError):
        judge_job("We are seeking a QA engineer.", fake_error)