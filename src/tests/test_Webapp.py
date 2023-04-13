import pytest
import numpy
import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import src.BMI.BMICalc as BMI
import src.Webapp.app as Webapp
from src.flaskr import create_app

# Webapp.createApp()

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_hello_world(client):
    response = client.get("/hello")
    assert b"Hello, World!" in response.data

