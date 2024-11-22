import requests
import allure

from user import User
from data import URL
from helpers import Generators


class Order:
    def create_order(self, ingredient: list, authorized_status=True):
        access_token = User().create_user(Generators().email, Generators().password, Generators().name)[1][
            'accessToken']
        if authorized_status is False:
            access_token = ''
        data = {
            'ingredients': ingredient
        }
        response = requests.post(f"{URL.BASE}{URL.CREATE_ORDER}", headers=access_token, json=data)
        return response.status_code, response.json(), access_token

    def get_user_order(self, authorized_status=True):
        access_token = User().create_user(Generators().email, Generators().password, Generators().name)[1][
            'accessToken']
        if authorized_status is False:
            access_token = ''
        response = requests.get(f"{URL.BASE}{URL.CREATE_ORDER}", headers=access_token)
        return response.status_code, response.json()