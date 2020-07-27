from time import *


class Timer:
    __func = None

    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        start = time()
        ret = self.__func(self, *args, **kwargs)
        print("elapsed_time:{0}nsec".format((time() - start) * 1024 * 1024 * 1024))
        return ret


class Squared:
    __func = None

    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        ret = self.__func(*args, **kwargs)
        return ret * ret


class Calculator:
    @Timer
    @Squared
    def sum(self, x: int, y: int):
        return x + y
