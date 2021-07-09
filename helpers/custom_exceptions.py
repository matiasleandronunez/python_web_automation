from abc import ABC


class RequestUnexpected(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class RequestReturnedNonOK(RequestUnexpected):
    def __init__(self, status_code):
        super().__init__(f"request returned a HTTP response code other than OK: {status_code}")


class RequestReturnedNonExpected(RequestUnexpected):
    def __init__(self, status_code):
        super().__init__(f"request returned a HTTP response code other than the expected. Was: {status_code}")
