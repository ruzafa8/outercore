import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function that generates a random ID for a student."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student."""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=True, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """Method that initializes the login attribute."""
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
