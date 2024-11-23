class URL:
    BASE = 'https://stellarburgers.nomoreparties.site/api'
    # User
    CREATE_USER = '/auth/register'
    LOGIN_USER = '/auth/login'
    CHANGE_USER = '/auth/user'
    # Order
    CREATE_ORDER = '/orders'


class DataUser:
    USER_1 = {"email": "hicksbobby@example.com", "password": "_3MQRAVw", "name": "klucas"}
    USER_2 = {"email": "charlesbell@example.net", "password": "_*8BmBwF", "name": "sharonsmith"}

    # TestCreateUser
    RESULT_MESSAGE_REGISTERED_USER = "User already exists"
    RESULT_MESSAGE_REQUIRED_FIELDS = "Email, password and name are required fields"
    # TestLoginUser
    RESULT_MESSAGE_WRONG_LOGIN = "email or password are incorrect"
    # TestChangeDataUser
    RESULT_MESSAGE_USER_UNAUTHORIZED = "You should be authorised"

    CASE_CREATE_USER = {1: "Создание пользователя без указания поля - Пароль",
                        2: "Создание пользователя без указания поля - Имя и Пароль"
                        }


class DataOrder:
    DICT_INGRIDIENTS = {
        "Флюоресцентная булка R2-D3": "61c0c5a71d1f82001bdaaa6d",
        "Мясо бессмертных моллюсков Protostomia": "61c0c5a71d1f82001bdaaa6f",
        "Говяжий метеорит (отбивная)": "61c0c5a71d1f82001bdaaa70",
        "Биокотлета из марсианской Магнолии": "61c0c5a71d1f82001bdaaa71",
        "Соус Spicy-X": "61c0c5a71d1f82001bdaaa72",
        "Филе Люминесцентного тетраодонтимформа": "61c0c5a71d1f82001bdaaa6e",
        "Соус фирменный Space Sauce": "61c0c5a71d1f82001bdaaa73",
        "Соус традиционный галактический": "61c0c5a71d1f82001bdaaa74",
        "Краторная булка N-200i": "61c0c5a71d1f82001bdaaa6c",
        "Соус с шипами Антарианского плоскоходца": "61c0c5a71d1f82001bdaaa75",
        "Хрустящие минеральные кольца": "61c0c5a71d1f82001bdaaa76",
        "Плоды Фалленианского дерева": "61c0c5a71d1f82001bdaaa77",
        "Кристаллы марсианских альфа-сахаридов": "61c0c5a71d1f82001bdaaa78",
        "Мини-салат Экзо-Плантаго": "61c0c5a71d1f82001bdaaa79",
        "Сыр с астероидной плесенью": "61c0c5a71d1f82001bdaaa7a",
    }

    RESULT_MESSAGE_UPSET_INGREDIENTS = 'Ingredient ids must be provided'

    CASE_CREATE = {1: "Создание заказа с авторизацией",
                   2: "Создание заказа без авторизации",
                   3: "Создание заказов без ингредиентов",
                   4: "Создание заказов с неверным хэшом ингредиентов"}

    CASE_GET = {1: "Получение заказа авторизированным пользователем",
                2: "Получение заказа без авторизации"}
