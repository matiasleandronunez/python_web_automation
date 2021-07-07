from enum import Enum

class Customer():
    def __init__(self, name=None, addr=None, email=None, phone=None, username=None, password=None, enabled=None, role=None):
        self.name = name
        self.addr = addr
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.enabled = enabled
        self.role = Role(1) if role == "USER" else Role(0)

class Role(Enum):
    UNKNOWN = 0
    USER = 1