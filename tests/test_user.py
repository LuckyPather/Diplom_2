import pytest
import allure

from methods.user import User
from helpers import Generators
from data import DataUser

# TODO: start method, teardown method, allure


class TestCreateUser:
    def test_create_new_user(self):
        user = User()
        data = Generators()
        response = user.create_user(data.email, data.password, data.name)
        print(response)
        assert response[0] == 200 and response[1]['success'] is True

    def test_create_registered_user(self):
        user = User()
        response = user.create_user(DataUser.USER_1["email"], DataUser.USER_1["password"], DataUser.USER_1["name"])
        print(response)
        assert response[0] == 403 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_REGISTERED_USER

    @pytest.mark.parametrize('email, password, name', [
        (DataUser.USER_1["email"], DataUser.USER_1["password"], ""),
        ("sdfs.yandex.ru", "", "")
    ])
    def test_create_user_without_requirements_field(self, email, password, name):
        user = User()
        response = user.create_user(email, password, name)
        print(response)
        assert response[0] == 403 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_REQUIRED_FIELDS


class TestLoginUser:
    @pytest.mark.parametrize('email, password', [
        (DataUser.USER_1["email"], DataUser.USER_1["password"]),
        (DataUser.USER_2["email"], DataUser.USER_2["password"])
    ])
    def test_login(self, email, password):
        user = User()
        response = user.login_user(email, password)
        print(response)
        assert response[0] == 200 and response[1]['success'] is True and response[1]['user']['email'] == email

    @pytest.mark.parametrize('email, password', [
        (DataUser.USER_1["email"], "wrong_password"),
        ("wrong_email", DataUser.USER_2["password"])
    ])
    def test_wrong_login(self, email, password):
        user = User()
        response = user.login_user(email, password)
        print(response)
        assert response[0] == 401 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_WRONG_LOGIN


class TestChangeDataUser:
    @pytest.mark.parametrize('email, password, login, new_email, new_name', [
        (Generators().email, Generators().password, Generators().name, Generators().email, Generators().name),
        (Generators().email, Generators().password, Generators().name, Generators().email, Generators().name)
    ])
    def test_change_user_data_authorized(self, email, password, login, new_email, new_name):
        user = User()
        response = user.change_user(email, password, login, new_email, new_name)
        assert response[0] == 200 and response[1]['success'] is True and response[1]['user']['email'] == new_email and \
               response[1]['user']['name'] == new_name

    @pytest.mark.parametrize('email, password, login, new_email, new_name, login_status', [
        (Generators().email, Generators().password, Generators().name, Generators().email, Generators().name, False),
        (Generators().email, Generators().password, Generators().name, Generators().email, Generators().name, False)
    ])
    def test_change_user_data_unauthorized(self, email, password, login, new_email, new_name, login_status):
        user = User()
        response = user.change_user(email, password, login, new_email, new_name, login_status)
        assert response[0] == 401 and response[1]['success'] is False and response[1][
            'message'] == DataUser.RESULT_MESSAGE_CHANGE_USER_UNAUTHORIZED
