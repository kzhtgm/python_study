import pytest

from python_study.Observer import Publisher


def test_observe():
    ret = Publisher().publish()
    assert len(ret) == 2
    assert ret[0] == "called ObserverA"
    assert ret[1] == "called ObserverB"
