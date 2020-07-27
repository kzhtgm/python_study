import threading
from abc import ABC


class Singleton(ABC):
    _unique_instance = None
    _lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This class is singleton. Use get_instance method.')

    @classmethod
    def get_instance(cls):
        # Double Checked Locking
        if not cls._unique_instance:
            with cls._lock:
                if not cls._unique_instance:
                    cls._unique_instance = super().__new__(cls)

        return cls._unique_instance


class ConcreteSingleton(Singleton):
    def __new__(cls, *args, **kwargs):
        pass
