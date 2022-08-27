# 4th layer
from flask import abort, jsonify, make_response, request

from . import use_cases
from .utils import exceptions as business_exception


def account_balance(account_number):
    try:
        account = use_cases.get_account_balance(account_number)
    except business_exception.AccountNotFoundError as error:
        abort(
            make_response(
                jsonify(
                    message=f"{error}"
                ), 
                404
            )
        )
    return account.representation()


def transfer_account_balance(from_account_number):
    request_data = request.get_json()
    amount = request_data.get('amount', None)
    to_account_number = request_data.get('to_account_number', None)
    
    error_message = None
    status_code = 0

    if (not amount) or (not to_account_number):
        abort(
            make_response(
                jsonify(
                    message="amount and to_account_number are required on POST request!"
                ), 
                400
            )
        )

    try:
        use_cases.transfer_balance(
            from_account_number, 
            to_account_number, 
            amount
        )
    except business_exception.AccountNotFoundError as error:
        error_message = error
        status_code = 404
    except business_exception.InsufficientBalanceError as error:
        error_message = error
        status_code = 400
    except business_exception.ForbiddenTransferError as error:
        error_message = error
        status_code = 400
    except TypeError as error:
        error_message = "Amount should be number!"
        status_code = 400

    if error_message:
        abort(
            make_response(
                jsonify(
                    message=f"{error_message}"
                ), 
                status_code
            )
        )
    
    return "", 201
