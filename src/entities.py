# 1st layer
from __future__ import annotations
from .utils.exceptions import ForbiddenTransferError, InsufficientBalanceError

class Customer:
    def __init__(self, customer_number: str, name: str):
        self.customer_number = customer_number
        self.name = name


class Account:
    def __init__(self, account_number: str, customer: Customer, balance: int):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def representation(self) -> dict:
        return {
            "account_number": self.account_number,
            "balance": self.balance,
            "customer_name": self.customer.name
        }

    def add_balance(self, amount: int):
        self.balance += amount
        
    def substract_balance(self, amount: int):
        self.balance -= amount

    def transfer_balance(self, to_account: Account, amount: int):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"{self.account_number}'s balance is {self.balance}, " 
                f"but you tried to transfer with the higher amount {amount}"
            )

        if amount < 0:
            raise ForbiddenTransferError(
                f"Can not transfer negative amount!"
            )

        if self.account_number == to_account.account_number:
            raise ForbiddenTransferError(
                f"Can not transfer to itself!"
            )

        self.substract_balance(amount)
        to_account.add_balance(amount)

        return to_account
