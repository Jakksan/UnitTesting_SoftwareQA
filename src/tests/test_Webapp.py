import pytest
import numpy
import sys
from pathlib import Path
from flask import Flask, request

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import src.BMI.BMICalc as BMI
import src.flaskr.Webapp.app as Webapp
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


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()


def test_request_hello_world(client):
    response = client.get("/hello")
    assert b"Hello, World!" in response.data

def test_request_index(client):
    response = client.get("/")
    assert b"BMI Calculator" in response.data

def test_request_data(client):
    response = client.get("/data")
    assert b"The URL /data is accessed directly." in response.data

def test_website_bmi_calc(client):
    send_data = {"lbs":"141", "ft":"5", "in":"8"}
    response = client.post('/data', data=send_data)
    assert response.status_code == 200
    assert b"21.437" in response.data
    assert b"Normal Weight" in response.data