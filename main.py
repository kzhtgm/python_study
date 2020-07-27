# from point import Point
from time import *


def time_measurement(self):
    def wrapper(*args, **kwargs):
        start = time()
        ret = self(*args, **kwargs)
        print("elapsed_time:{0}nsec".format((time() - start) * 1024 * 1024 * 1024))
        return ret

    return wrapper


@time_measurement
def main():
    pass


if __name__ == '__main__':
    main()
