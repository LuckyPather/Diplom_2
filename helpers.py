from faker import Faker
from data import DataOrder


class Generators:

    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.password = fake.password(length=8)
        self.name = fake.user_name()


def return_hash(numbers: list):
    ingredient_hash_list = list(DataOrder.DICT_INGRIDIENTS.values())
    selected_ingredient = []
    for i in numbers:
        selected_ingredient.append(ingredient_hash_list[i])
    return selected_ingredient
