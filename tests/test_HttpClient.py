import pytest

from python_study.HttpClient import HttpClient


def test_get():
    content = HttpClient.get()
    json: dict = content.json()["data"]
    assert json["pref"] == "東京都"
    assert json["city"] == "千代田区"
    assert json["town"] == "千代田"
    assert json["address"] == "千代田区千代田"
    assert json['fullAddress'] == "東京都千代田区千代田"


