import pytest

from python_study import Singleton
from python_study.Singleton import ConcreteSingleton


def test_singleton():
    obj1: Singleton = ConcreteSingleton.get_instance()
    obj2: Singleton = ConcreteSingleton.get_instance()

    assert obj1 is obj2
