import urllib

import requests


class ClientException(Exception):
    pass


class ServerException(Exception):
    pass


class Content:
    __response = None

    def __init__(self, response):
        self.__response = response

    def json(self) -> dict:
        return self.__response.json()

    def status_code(self) -> int:
        return self.__response.status_code

    def text(self) -> str:
        return self.__response.text


class HttpClient:
    @staticmethod
    def get() -> Content:
        response = requests.get('https://api.zipaddress.net?zipcode=1000001')
        HttpClient.is_ok(response.status_code)

        return Content(response)

    @staticmethod
    def is_ok(status_code: int) -> bool:
        if 200 <= status_code < 400:
            return True
        elif 400 <= status_code < 500:
            raise ClientException()
        elif status_code >= 500:
            raise ServerException()
        else:
            raise Exception()

    @staticmethod
    def post():
        response = requests.post('https://www.yahoo.co.jp', data={})
        print(response.status_code)
        print(response.text)
