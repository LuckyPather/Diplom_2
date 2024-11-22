from faker import Faker


class Generators:

    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.password = fake.password(length=8)
        self.name = fake.user_name()
