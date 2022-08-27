# Simple Aja
Simple rest API for getting user balance and transfer balance to another user.

## Prerequire
- Docker Compose Installed [https://docs.docker.com/compose/install/]
- Make sure Docker and Docker Compose are running

## First Run
- build the docker images
- run command: `docker compose build` 

## Run Tests
run command: `docker compose run simple-aja pytest`

## Show Tests Coverage
run command: `docker compose run simple-aja coverage run -m pytest`

run command: `docker compose run simple-aja coverage report`

## Run locally
- extract the zipfile
- change directory to simple-aja folder 
- run command: `docker compose up`
- check if the service is ready, visit `http://127.0.0.1:8000/`
- get `http://127.0.0.1:8000/initiate-db` to initiate or reset db data

## Available Endpoints
- GET /account/{account_number}
```
success response:
{
    "account_number" : "555001", 
    "customer_name" : "Bob Martin", 
    "balance" : 10000
}
status_code 200
```
- POST /account/{from_account_number}/transfer
```
request body:
{
    "to_account_number" : "555002", 
    "amount" : 100
}

success response:
status_code 201
```