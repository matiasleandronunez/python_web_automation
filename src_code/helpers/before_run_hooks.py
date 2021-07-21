#Clear for new execution and set data, cant use hook because of parallel execution hack
from helpers import apihelper
from helpers.custom_exceptions import RequestUnexpected


def setup_before_run():
    try:
        apihelper.delete_all_customers()
    except RequestUnexpected:
        #Abort execution
        raise KeyboardInterrupt()