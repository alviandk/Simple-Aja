import pytest

from src import use_cases
from src.databases import init_db
from src.utils import exceptions


def test_get_account_balance():
    account = use_cases.get_account_balance('555001')
    assert account.account_number == '555001'
    assert account.balance == 10000


def test_get_account_balance_not_found():
    with pytest.raises(
        exceptions.AccountNotFoundError,
        match='Account 000 does not exist on database'
    ):
        use_cases.get_account_balance('000')


def test_transfer_balance():
    account1 = use_cases.get_account_balance('555001')
    account2 = use_cases.get_account_balance('555002')

    # no exception means everything is all right
    use_cases.transfer_balance(account1.account_number, account2.account_number, 100)

    # revert db after mutate
    init_db.inititate()