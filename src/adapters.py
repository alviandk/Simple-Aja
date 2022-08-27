# 3rd layer
from .entities import Account, Customer
from typing import List
from .utils.exceptions import AccountNotFoundError
from .databases.db_connections import get_db_connection


def query_get_customer_account(account_number: str):
    # query to dict
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT"
        f" accounts.account_number, accounts.customer_number, accounts.balance, customers.name"
        f" FROM accounts"
        f" INNER JOIN customers"
        f" ON customers.customer_number = accounts.customer_number"
        f" WHERE accounts.account_number = '{account_number}'"
        f";"
    );
    accounts = cur.fetchall()
    cur.close()
    conn.close()

    if not accounts:
        raise AccountNotFoundError(
            f"Account {account_number} does not exist on database"
        )

    account = accounts[0]
    print("account", account)
    customer_account = {
        "customer_number": account[1],
        "name": account[3],
        "account_number": account[0],
        "balance": account[2],
    }
    
    customer  = Customer(
        customer_account["customer_number"],
        customer_account["name"],
    )
    
    return Account(
        customer_account["account_number"],
        customer,
        customer_account["balance"]
    )


def account_commit_db(account : Account):
    # commit changes db accounts

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        f"UPDATE accounts"
        f" SET balance={account.balance}"
        f" WHERE account_number = '{account.account_number}'"
        f";"
    );
    conn.commit()
    cur.close()
    conn.close()
