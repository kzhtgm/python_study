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


def test_インスタンスメソッドをモックに差し替え(mocker):
    # ①：インスタンスレベルで振る舞い差し替え
    title = GroupManager()
    mocker.patch.object(title, "calc_salary", return_value=120)
    assert title.calc_salary() == 120

    # ②：①の差し替えはインスタンスレベルなので、インスタンスが違えば振る舞いは引き継がれない
    title = GroupManager()
    assert title.calc_salary() == 100

    # ③：クラスレベルで振る舞い差し替え
    # クラスレベルなので②と同じインスタンスだとしても振る舞いは変わってしまう。
    mocker.patch.object(GroupManager, "calc_salary", return_value=130)
    assert title.calc_salary() == 130

    # ④：新しいインスタンスを作っても③の振る舞いは引き継がれる。
    title = GroupManager()
    assert title.calc_salary() == 130

    # ⑤：③でクラスレベルで振る舞いを定義してもモックは影響を受けない
    # モックに振る舞いを定義していないので、100 でさえない
    title_mock = mocker.Mock()
    assert title_mock.calc_salary() != 130
    assert title_mock.calc_salary() != 100

    attrs = {"calc_salary.return_value": 120}
    title_mock.configure_mock(**attrs)
    assert title_mock.calc_salary() == 120


def test_reset_mock(mocker):
    title_mock: GroupManager = mocker.Mock()
    mocker.patch.object(title_mock, "calc_salary", return_value=140)

    assert title_mock.calc_salary() == 140
    # return_value=True にしたらリセットされるって書いてあるけどされない...
    title_mock.reset_mock(return_value=True)
    assert title_mock.calc_salary() != 100


def test_method_call(mocker):
    receive = mocker.patch("python_study.TemplateMethod.GroupManager._title_name")
    title: Title = GroupManager()
    title.calc_salary()
    assert len(receive.call_args_list) == 0

    title.template_method()
    assert len(receive.call_args_list) == 1

    title = GroupManager()
    title.template_method()
    assert len(receive.call_args_list) == 2
