import random
from collections.abc import Iterator
from typing import NamedTuple

from faker import Faker


class User(NamedTuple):
    login: str
    email: str
    password: str

    def __str__(self):
        return f"{self.login} {self.email} {self.password}"

    __repr__ = __str__


faker = Faker()


def generate_user() -> User:
    profile = faker.profile()
    return User(
        login=profile["username"],
        email=profile["mail"],
        password=faker.password(random.randint(10, 20)),
    )


def generate_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
