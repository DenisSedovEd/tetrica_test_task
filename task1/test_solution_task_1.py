import re

import pytest
# from solution import sum_two
from solution import strict


@strict
def sum_two_digit(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_str(a: str, b: str) -> str:
    return a + b


class TestSolution:

    @pytest.mark.parametrize(
        'a, b',
        [
            ('1', 2),
            (1, '2'),
            ('1', '2'),
        ]
    )
    def test_sum_two_digit_with_raise(self, a, b):
        with pytest.raises(
                TypeError,
        ) as exc_info:
            sum_two_digit(a, b)
            assert exc_info.type is TypeError

    def test_sum_two_digit_correctly(self):
        res = sum_two_digit(1, 2)
        expected = 3
        assert res == expected


    @pytest.mark.parametrize(
        'a, b',
        [
            ('1',2),
            (1,'2'),
            (1,2),
        ]
    )
    def test_two_str_with_raise(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            sum_two_str(a, b)
            assert exc_info.type is TypeError

    def test_two_str_correct(self):
        res = sum_two_str('1', '2')
        expected = '12'
        assert res == expected