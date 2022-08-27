# 5th layer
from flask import Flask

from . import controllers
from .databases import init_db

app = Flask(__name__)


@app.route('/')
def index():
    return "ready"

@app.route('/initiate-db')
def initiate_db():
    init_db.inititate()
    return "database inittiated"


@app.route('/account/<string:account_number>', methods=['GET'])
def account_balance(account_number):
    return controllers.account_balance(account_number)


@app.route('/account/<string:from_account_number>/transfer', methods=['POST'])
def transfer_account_balance(from_account_number):
    return controllers.transfer_account_balance(from_account_number)
