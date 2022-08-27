import pytest

from src import adapters, entities
from src.databases import init_db
from src.utils import exceptions


def test_query_get_customer_account_type_return():
    account = adapters.query_get_customer_account('555002')
    assert type(account) == entities.Account


def test_query_get_customer_account():
    account = adapters.query_get_customer_account('555002')
    assert account.account_number == '555002'


def test_query_get_customer_account_not_exist():
    with pytest.raises(
        exceptions.AccountNotFoundError,
        match='Account 111 does not exist on database'
    ):
        adapters.query_get_customer_account('111')


def test_account_commit_db():
    account_initial = adapters.query_get_customer_account('555002')
    initial_balance = account_initial.balance
    
    account_initial.add_balance(100)
    adapters.account_commit_db(account_initial)

    account_after_commit = adapters.query_get_customer_account('555002')
    assert account_after_commit.balance == initial_balance + 100

    # revert db after mutate
    init_db.inititate()
