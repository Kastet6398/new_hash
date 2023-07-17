import pytest

import crypto_lib

test_cases_md5 = [
    ("qwerty", "d8578edf8458ce06fbc5bb76a58c5ca4"),
    ('srjtyusryt734476583574', '127020bf98da7b018bc6deb1633d21a3'),
]


@pytest.mark.parametrize('value, expected', test_cases_md5)
def test_encode_md5(value, expected):
    assert crypto_lib.encode_md5(value) == expected
