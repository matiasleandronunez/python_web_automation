import string
from enum import Enum
import random
from faker import Faker

class Customer():
    def __init__(self, name=None, addr=None, email=None, phone=None, username=None, password=None, enabled=None, role=None):
        faker = Faker()

        self.name = name if name else faker.name()
        self.addr = addr if addr else faker.address()
        self.email = email if email else faker.email()
        self.phone = phone if phone else faker.phone_number()
        self.username = username if username else ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        self.password = password if password else ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        self.enabled = enabled
        self.role = Role(1) if role == "USER" else Role(0)

class Role(Enum):
    UNKNOWN = 0
    USER = 1