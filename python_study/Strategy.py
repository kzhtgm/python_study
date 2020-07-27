import re
from abc import abstractmethod, ABC
from typing import Optional, Match, AnyStr


class TextStrategy(ABC):
    def validate(self, text: str) -> Optional[Match[AnyStr]]:
        return self.regex().fullmatch(text)

    @abstractmethod
    def regex(self) -> re:
        pass


class TextBox:
    __strategy: TextStrategy = None

    def __init__(self, strategy: TextStrategy):
        self.__strategy = strategy

    def validate(self, text: str) -> Optional[Match[AnyStr]]:
        return self.__strategy.validate(text)


class NumericStrategy(TextStrategy):
    __regex: re = re.compile("[\\d]*")

    def regex(self) -> re:
        return self.__regex


class AlphaNumericStrategy(TextStrategy):
    __regex: re = re.compile("[a-zA-Z0-9]*")

    def regex(self) -> re:
        return self.__regex


class TextStrategyFactory:
    @staticmethod
    def create_strategy(strategy: str) -> TextStrategy:
        if strategy == "Numeric":
            return NumericStrategy()
        elif strategy == "AlphaNumeric":
            return AlphaNumericStrategy()
        else:
            raise Exception("Unsupported strategy.")
