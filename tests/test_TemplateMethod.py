import pytest

from python_study.TemplateMethod import GroupManager, SeniorManager, Title


def test_group_manager_salary():
    title = GroupManager()
    assert title.calc_salary() == 100


def test_template_method():
    title: Title = GroupManager()
    assert title.template_method() == "GroupManager template method called."


def test_senior_manager_salary():
    title = SeniorManager()
    assert title.calc_salary() == 200


def test_mangling():
    title = GroupManager()

    # __ をプレフィックスにしてもマングリングされるだけなので、その気になれば見えてしまう
    assert title._GroupManager__name == "default name"
