# 2nd layer
from . import adapters

from .entities import Account


def transfer_balance(from_account_number: str, to_account_number: str, amount: int):
    from_account = adapters.query_get_customer_account(from_account_number)
    to_account = adapters.query_get_customer_account(to_account_number)
    
    to_account_after = from_account.transfer_balance(to_account, amount)
 
    adapters.account_commit_db(from_account)
    adapters.account_commit_db(to_account_after)


def get_account_balance(account_number: str) -> Account:
    account = adapters.query_get_customer_account(account_number)

    return account
