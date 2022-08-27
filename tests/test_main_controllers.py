from src.databases import init_db


def test_root_healthy(client):
    response = client.get("/")
    assert response.status_code == 200


def test_initiate_db(client):
    response = client.get("/initiate-db")
    assert response.status_code == 200

 
def test_account_balance_bob(client):
    response = client.get("/account/555001")
    assert response.json == {
        "account_number": "555001",
        "balance": 10000,
        "customer_name": "Bob Martin"
    }
    assert response.status_code == 200

def test_account_balance_linus(client):
    response = client.get("/account/555002")
    assert response.json == {
        "account_number": "555002",
        "balance": 15000,
        "customer_name": "Linus Torvalds"
    }
    assert response.status_code == 200


def test_account_balance_not_exist(client):
    response = client.get("/account/123")
    assert response.json == {'message': 'Account 123 does not exist on database'}
    assert response.status_code == 404


def test_transfer_account_balance_from_not_exist(client):
    response = client.post(
        "/account/345/transfer",
        json = {
            "to_account_number" : "555002", 
            "amount" : 100
        }
    )
    assert response.json == {'message': 'Account 345 does not exist on database'}
    assert response.status_code == 404


def test_transfer_account_balance_to_not_exist(client):
    response = client.post(
        "/account/555002/transfer",
        json = {
            "to_account_number" : "678", 
            "amount" : 100
        }
    )
    assert response.json == {'message': 'Account 678 does not exist on database'}
    assert response.status_code == 404


def test_transfer_account_balance_amount_empty(client):
    response = client.post(
        "/account/555002/transfer",
        json = {
            "to_account_number" : "555001", 
        }
    )
    assert response.json == {
        "message": "amount and to_account_number are required on POST request!"
    }
    assert response.status_code == 400


def test_transfer_account_balance_to_empty(client):
    response = client.post(
        "/account/555002/transfer",
        json = {
            "amount" : "500", 
        }
    )
    assert response.json == {
        "message": "amount and to_account_number are required on POST request!"
    }
    assert response.status_code == 400


def test_transfer_account_balance_json_empty(client):
    response = client.post(
        "/account/555002/transfer",
        json={}
    )
    assert response.status_code == 400
    assert response.json == {
        "message": "amount and to_account_number are required on POST request!"
    }
    

def test_transfer_account_balance_insufficients(client):
    response = client.post(
        "/account/555002/transfer",
        json = {
            "to_account_number" : "555001", 
            "amount" : 100000000
        }
    )
    assert response.json == {
        "message": "555002's balance is 15000, but you tried to transfer with the higher amount 100000000"
    }
    assert response.status_code == 400


def test_transfer_account_balance_to_itself(client):
    response = client.post(
        "/account/555002/transfer",
        json = {
            "to_account_number" : "555002", 
            "amount" : 100
        }
    )
    assert response.json == {
        "message": "Can not transfer to itself!"
    }
    assert response.status_code == 400


def test_transfer_account_balance_negative_amount(client):
    response = client.post(
        "/account/555001/transfer",
        json = {
            "to_account_number" : "555002", 
            "amount" : -10
        }
    )
    assert response.json == {
        "message": "Can not transfer negative amount!"
    }
    assert response.status_code == 400


def test_transfer_account_balance_amount_string(client):
    response = client.post(
        "/account/555001/transfer",
        json = {
            "to_account_number" : "555002", 
            "amount" : "abc"
        }
    )
    assert response.json == {
        "message": "Amount should be number!"
    }
    assert response.status_code == 400


def test_transfer_account_balance(client):
    response = client.post(
        "/account/555001/transfer",
        json = {
            "to_account_number" : "555002", 
            "amount" : 100
        }
    )
    assert response.status_code == 201

    response = client.get("/account/555001")
    assert response.json == {
        "account_number": "555001",
        "balance": 10000 - 100,
        "customer_name": "Bob Martin"
    }

    response = client.get("/account/555002")
    assert response.json == {
        "account_number": "555002",
        "balance": 15000 + 100,
        "customer_name": "Linus Torvalds"
    }

    # revert db after mutate
    init_db.inititate()
