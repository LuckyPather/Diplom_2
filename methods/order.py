import requests
import allure

from methods.user import User
from data import URL


class Order:
    def create_order(self, ingredient: list, email, password, authorized_status=True):
        with allure.step(f"Захожу под пользователем {email}, {password} и получаю токен"):
            access_token = User().login_user(email, password)[1]['accessToken']
        if authorized_status is False:
            access_token = ''
        data = {
            'ingredients': ingredient
        }
        with allure.step("Создаю новый заказ"):
            response = requests.post(f"{URL.BASE}{URL.CREATE_ORDER}", headers={"Authorization": f"{access_token}"},
                                     json=data)
        if response.status_code == 500:
            return response.status_code
        else:
            return response.status_code, response.json(), access_token

    def get_user_order(self, email, password, authorized_status=True):
        with allure.step(f"Захожу под пользователем {email}, {password} и получаю токен"):
            access_token = User().login_user(email, password, )[1]['accessToken']
        if authorized_status is False:
            access_token = ''
        with allure.step("Получаю заказы пользователя"):
            response = requests.get(f"{URL.BASE}{URL.CREATE_ORDER}", headers={"Authorization": f"{access_token}"})
        return response.status_code, response.json()
