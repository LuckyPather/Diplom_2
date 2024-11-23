import pytest
import allure

from methods.user import User
from helpers import Generators
from data import DataUser


@allure.suite("Пользователь")
@allure.sub_suite("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание нового пользователя")
    def test_create_new_user(self, create_user, delete_user):
        assert create_user[3][0] == 200 and create_user[3][1]['success'] is True

    @allure.title("Попытка создать, уже зарегистрированного пользователя")
    def test_create_registered_user(self):
        user = User()
        response = user.create_user(DataUser.USER_1["email"], DataUser.USER_1["password"], DataUser.USER_1["name"])
        assert response[0] == 403 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_REGISTERED_USER

    @pytest.mark.parametrize('case, email, password, name', [
        (DataUser.CASE_CREATE_USER[2], DataUser.USER_1["email"], DataUser.USER_1["password"], ""),
        (DataUser.CASE_CREATE_USER[1], "sdfs.yandex.ru", "", "")
    ],
                             ids=[
                                 "Creating a user without specifying the - Password field",
                                 "Creating a user without specifying the - Name and Password fields"
                             ])
    def test_create_user_without_requirements_field(self, case, email, password, name):
        allure.dynamic.title(case)
        user = User()
        response = user.create_user(email, password, name)
        assert response[0] == 403 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_REQUIRED_FIELDS


@allure.suite("Пользователь")
@allure.sub_suite("Вход в аккаунт")
class TestLoginUser:
    @pytest.mark.parametrize('email, password', [
        (DataUser.USER_1["email"], DataUser.USER_1["password"]),
        (DataUser.USER_2["email"], DataUser.USER_2["password"])
    ],
                             ids=[
                                 "Login as user 1",
                                 "Login as user 2"
                             ])
    @allure.title("Вход с валидными данными")
    def test_login(self, email, password):
        user = User()
        response = user.login_user(email, password)
        print(response)
        assert response[0] == 200 and response[1]['success'] is True and response[1]['user']['email'] == email

    @pytest.mark.parametrize('email, password', [
        (DataUser.USER_1["email"], "wrong_password"),
        ("wrong_email", DataUser.USER_2["password"])
    ],
                             ids=[
                                 "Login with incorrect password",
                                 "Login with incorrect email"
                             ])
    @allure.title("Вход с невалидными данными")
    def test_wrong_login(self, email, password):
        user = User()
        response = user.login_user(email, password)
        print(response)
        assert response[0] == 401 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_WRONG_LOGIN


@allure.suite("Пользователь")
@allure.sub_suite("Изменение данных пользователя")
class TestChangeDataUser:

    @allure.title("Изменение данных авторизованного пользователя")
    @pytest.mark.flaky(reruns=1)
    def test_change_user_data_authorized(self, create_user, delete_user):
        user = User()
        new_data_user = Generators()
        response = user.change_user(create_user[3][1]['accessToken'], create_user[1], create_user[2],
                                    new_data_user.email,
                                    new_data_user.name)
        assert response[0] == 200 and response[1]['success'] is True and response[1]['user'][
            'email'] == new_data_user.email and \
               response[1]['user']['name'] == new_data_user.name

    @allure.title("Изменение данных НЕ авторизованного пользователя")
    @pytest.mark.flaky(reruns=1)
    def test_change_user_data_unauthorized(self, create_user, delete_user):
        user = User()
        new_data_user = Generators()
        response = user.change_user(create_user[3][1]['accessToken'], create_user[1], create_user[2],
                                    new_data_user.email,
                                    new_data_user.name, login_status=False)
        assert response[0] == 401 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_USER_UNAUTHORIZED
