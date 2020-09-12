from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def observe(self):
        pass


class ObserverA(Observer):
    def observe(self):
        return "called ObserverA"


class ObserverB(Observer):
    def observe(self):
        return "called ObserverB"


class Publisher:
    __observers = None

    def __init__(self):
        self.__observers = [ObserverA(), ObserverB()]

    def publish(self) -> bool:
        #     ret = []
        #     for observer in self.__observers:
        #         ret.append(observer.observe())
        #     return ret
        return [observer.observe() for observer in self.__observers]
