import pytest

from src import main
from src.databases import init_db

@pytest.fixture()
def app():
    # other setup can go here
    init_db.inititate()
    app = main.app
    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
