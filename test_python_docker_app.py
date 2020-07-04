# test_python-docker-app.py
import pytest
from python_docker_app import app

def test_python_docker_app_1():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello World!'

def test_python_docker_app_2():
    response = app.test_client().get('/Sumanta')

    assert response.status_code == 200
    assert response.data == b'Hello Sumanta!'
    
