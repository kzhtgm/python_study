import pytest

from python_study.Strategy import NumericStrategy, AlphaNumericStrategy, TextBox, TextStrategyFactory


def test_numeric_strategy_ok():
    strategy = NumericStrategy()

    assert strategy.validate("5353") is not None
    assert strategy.validate("kazuhito") is None


def test_alpha_numeric_strategy_ok():
    strategy = AlphaNumericStrategy()

    assert strategy.validate("kazuhito") is not None
    assert strategy.validate("5353") is not None
    assert strategy.validate("kazuhito53") is not None
    assert strategy.validate("kazuhitoが") is None


def test_strategy_factory_ok():
    assert isinstance(TextStrategyFactory.create_strategy("Numeric"), NumericStrategy)
    assert isinstance(TextStrategyFactory.create_strategy("AlphaNumeric"), AlphaNumericStrategy)


def test_strategy_factory_unsupported():
    with pytest.raises(Exception):
        TextStrategyFactory.create_strategy("hoge")


def test_text_box():
    strategy = TextStrategyFactory.create_strategy("Numeric")
    text_box = TextBox(strategy)
    assert text_box.validate("5353") is not None
    assert text_box.validate("53k") is None
