import allure
import pytest

from methods.order import Order
from data import DataUser, DataOrder
from helpers import return_hash


@allure.suite("Заказы")
@allure.sub_suite("Создание и получение списка заказов")
class TestOrder:
    @pytest.mark.parametrize(
        'case, ingredient, email, password, authorized_status, status_code, result_status, message', [
            (DataOrder.CASE_CREATE[1], return_hash([0, 1, 2]), DataUser.USER_1['email'], DataUser.USER_1['password'],
             True, 200, True, None),
            (DataOrder.CASE_CREATE[2], return_hash([0, 1, 6]), DataUser.USER_1['email'], DataUser.USER_1['password'],
             False, 200, True, None),
            (DataOrder.CASE_CREATE[3], [], DataUser.USER_1['email'], DataUser.USER_1['password'], True, 400, False,
             DataOrder.RESULT_MESSAGE_UPSET_INGREDIENTS),
            (DataOrder.CASE_CREATE[4], ["61c0c5a71d1001bdaaa6d", "0c5a71d1f8200"], DataUser.USER_1['email'],
             DataUser.USER_1['password'], True, 500,
             None, None)
        ],
        ids=[
            "Creating an order with authentication",
            "Creating an order without authentication",
            "Creating an order without ingredients",
            "Creating an order with incorrect ingredient hash"
        ])
    def test_create_order(self, case, ingredient, email, password, authorized_status, status_code, result_status,
                          message):
        allure.dynamic.title(case)
        order = Order()
        response = order.create_order(ingredient, email, password, authorized_status)
        match status_code:
            case 500:
                assert response == 500
            case 400:
                assert response[0] == status_code and response[1]['success'] == result_status and response[1][
                    'message'] == message
            case _:
                assert response[0] == status_code and response[1]['success'] == result_status

    @pytest.mark.parametrize("case, email, password, authorized_status", [
        (DataOrder.CASE_GET[1], DataUser.USER_1['email'], DataUser.USER_1['password'], True),
        (DataOrder.CASE_GET[2], DataUser.USER_1['email'], DataUser.USER_1['password'], False)
    ],
                             ids=[
                                 "Getting an order as an authorized user",
                                 "Getting an order without authorization"
                             ])
    def test_get_user_order(self, case, email, password, authorized_status):
        allure.dynamic.title(case)
        order = Order()
        response = order.get_user_order(email, password, authorized_status)
        if authorized_status:
            assert response[0] == 200 and response[1]['success'] is True
        else:
            assert response[0] == 401 and response[1]['success'] is False and response[1][
                'message'] == DataUser.RESULT_MESSAGE_USER_UNAUTHORIZED
