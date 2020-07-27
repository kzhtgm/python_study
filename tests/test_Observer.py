import pytest

from python_study.Observer import Publisher


def test_observe():
    assert Publisher().publish()
