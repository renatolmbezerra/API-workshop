import pytest

from fastapi.testclient import TestClient
from main import app

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

def test_tamanho_da_lista_produtos():
    """
    Testa a função listar_produtos.
    :return: None
    """
    response = client.get("/produtos")
    assert len(response.json()) == 4

def test_pega_um_produto():
    """
    Testa a função obter_produto.
    :return: None
    """
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Smartphone com tela de 6 polegadas e 128GB de armazenamento.",
        "preco": 1999.99,
        "disponivel": True,
        "categoria": "eletronicos",
    }