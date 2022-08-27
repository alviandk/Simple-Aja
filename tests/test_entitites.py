import pytest

from src import entities
from src.utils import exceptions


def test_add_balance():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    account1.add_balance(amount=100)
    account1.balance = 1100


def test_substract_balance():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    account1.substract_balance(amount=100)
    account1.balance = 900


def test_transfer():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    customer2 = entities.Customer(customer_number='234', name='tester2')
    account2 = entities.Account(account_number='567', customer=customer2, balance=2000)

    account2_after = account1.transfer_balance(to_account=account2, amount=100)
    assert account1.balance == 900
    assert account2_after.balance == 2100


def test_transfer_insufficient():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    customer2 = entities.Customer(customer_number='234', name='tester2')
    account2 = entities.Account(account_number='567', customer=customer2, balance=2000)

    with pytest.raises(
        exceptions.InsufficientBalanceError,
        match="456's balance is 1000, "
            "but you tried to transfer with the higher amount 1100"
    ):
        account1.transfer_balance(to_account=account2, amount=1100)


def test_transfer_to_itself():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    with pytest.raises(
        exceptions.ForbiddenTransferError, 
        match='Can not transfer to itself!'
    ):
        account1.transfer_balance(to_account=account1, amount=100)


def test_transfer_negative_amount():
    customer1 = entities.Customer(customer_number='123', name='tester')
    account1 = entities.Account(account_number='456', customer=customer1, balance=1000)

    customer2 = entities.Customer(customer_number='234', name='tester2')
    account2 = entities.Account(account_number='567', customer=customer2, balance=2000)

    with pytest.raises(
        exceptions.ForbiddenTransferError, 
        match='Can not transfer negative amount!'
    ):
        account1.transfer_balance(to_account=account2, amount=-100)
