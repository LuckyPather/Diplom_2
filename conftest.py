import pytest
import allure
import requests

from methods.user import User
from data import URL
from helpers import Generators


@pytest.fixture
@allure.step("Создаю пользователя")
def create_user():
    data_user = Generators()
    with allure.step(
            f"Создаю пользователя с данными email: {data_user.email}, password {data_user.password}, name {data_user.name}"):
        response = User().create_user(data_user.email, data_user.password, data_user.name)
    assert response[1]['accessToken'] is not None, "Ошибка создания пользователя"
    return data_user.email, data_user.password, data_user.name, response


@pytest.fixture
@allure.title("Удаляю созданного пользователя")
def delete_user(create_user):
    access_token = create_user[3][1]['accessToken']
    yield
    with allure.step(
            f"Удаляю пользователя с данными email: {create_user[0]}, password {create_user[1]}, name {create_user[2]}"):
        requests.delete(f"{URL.BASE}{URL.CHANGE_USER}", headers={"Authorization": f"{access_token}"})
