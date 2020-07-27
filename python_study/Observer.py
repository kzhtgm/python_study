from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def observe(self):
        pass


class ObserverA(Observer):
    def observe(self):
        print("ObserverA")


class ObserverB(Observer):
    def observe(self):
        print("ObserverB")


class Publisher:
    __observers = None

    def __init__(self):
        self.__observers = [ObserverA(), ObserverB()]

    def publish(self) -> bool:
        for observer in self.__observers:
            observer.observe()
        return True
