import requests
import allure

from data import URL


class User:

    def create_user(self, email, password, login):
        data = {
            "email": email,
            "password": password,
            "name": login
        }
        with allure.step(f"Создаю пользователя с данным Email: {email}, Пароль: {password}, Логин {login}"):
            response = requests.post(f"{URL.BASE}{URL.CREATE_USER}", json=data)
        return response.status_code, response.json()

    def login_user(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        with allure.step(f"Авторизуюсь с данными Email: {email}, Пароль: {password}"):
            response = requests.post(f"{URL.BASE}{URL.LOGIN_USER}", json=data)
        return response.status_code, response.json()

    def change_user(self, access_token, email, password, new_email, new_name, login_status=True):
        access_token = access_token

        if login_status is False:
            access_token = ""

        data = {
            "email": new_email,
            "name": new_name
        }
        with allure.step(f"Захожу под пользователем с данными - Email:{email} Password: {password}, меняю "
                         f"Email на:{new_email} password на"):
            response = requests.patch(f"{URL.BASE}{URL.CHANGE_USER}", headers={"Authorization": f"{access_token}"},
                                      json=data)
        return response.status_code, response.json()
