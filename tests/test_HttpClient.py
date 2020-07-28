from requests import Response

from python_study.HttpClient import HttpClient, Content


def test_get():
    content = HttpClient.get()
    json: dict = content.json()["data"]
    assert json["pref"] == "東京都"
    assert json["city"] == "千代田区"
    assert json["town"] == "千代田"
    assert json["address"] == "千代田区千代田"
    assert json['fullAddress'] == "東京都千代田区千代田"


def test_mock_requests_get(mocker):
    response_mock: Response = mocker.Mock()
    response_mock.status_code = 301
    response_mock.text = "kzhtgm"
    mocker.patch("requests.get").return_value = response_mock

    actual = HttpClient.get()
    assert actual.status_code() == 301
    assert actual.text() == "kzhtgm"


def test_mock_get(mocker):
    response_mock: Response = mocker.Mock()
    content = Content(response_mock)
    mocker.patch.object(HttpClient, "get", return_value=content)
    actual = HttpClient.get()
    assert actual is content
