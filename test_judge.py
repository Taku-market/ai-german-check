import pytest
from judge import parse_answer

@pytest.mark.parametrize("text, expected",[
    ('{"requires_german": true}', True),
    ('{"requires_german": false}', False),
    ('Yes, German is required.', None),
    ('', None),
    ('{"answer": true}', None),
])
def test_parse_answer(text, expected):
    assert parse_answer(text) == expected