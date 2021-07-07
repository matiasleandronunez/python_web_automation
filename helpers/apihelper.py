from context.config import settings
from types import SimpleNamespace
import requests
import json
from helpers.custom_exceptions import RequestReturnedNonOK, RequestReturnedNonExpected


def get_customer_by_username(username):
    response = requests.get(f"{settings.api_uri}/api/customer/username={username}")

    if response.status_code != 200:
        raise RequestReturnedNonOK(response.status_code)
    else:
        return json.loads(response.json(), object_hook=lambda d: SimpleNamespace(**d))

def get_login_token(customer):
    req_body = {
                "username": f"{customer.username}",
                "password": f"{customer.password}"
    }

    response = requests.post(f"{settings.api_uri}/login/", json=req_body)

    if response.status_code != 200:
        raise RequestReturnedNonOK(response.status_code)
    else:
        return response.status_code

def post_customer(customer):
    req_body = {"customerId": 0,
        "name": f"{customer.name}",
        "address": f"{customer.addr}",
        "email": f"{customer.email}",
        "phone": f"{customer.phone}",
        "username": f"{customer.username}",
        "password": f"{customer.password}",
        "enabled": "true",
        "role": "USER"}

    response = requests.post(f"{settings.api_uri}/api/customer/", json=req_body)

    if response.status_code != 200:
        raise RequestReturnedNonOK(response.status_code)
    else:
        return response.status_code

def delete_all_customers():
    response = requests.delete(f"{settings.api_uri}/api/customer/")

    if response.status_code != 204:
        raise RequestReturnedNonExpected(response.status_code)
    else:
        return response.status_code