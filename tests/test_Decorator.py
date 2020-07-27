import pytest

from python_study.Decorator import Calculator


def test_sum():
    calc = Calculator()
    assert calc.sum(2, 3) == 25
