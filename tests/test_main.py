from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ola_mundo():
    """
    Testa a função ola_mundo.
    :return: None
    """
    response = client.get("/")
    assert response.status_code == 200
    

def test_ola_mundo_json():
    """
    Testa a função ola_mundo.
    :return: None
    """
    response = client.get("/")
    assert response.json() == {"Olá": "Mundo"}

def test_listar_produtos_status_code():
    """
    Testa a função listar_produtos.
    :return: None
    """
    response = client.get("/produtos")
    assert response.status_code == 200
