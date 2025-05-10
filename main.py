from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def ola_mundo():
    """
    Função que retorna um dicionário com a chave "Ola" e o valor "Mundo".
    :return: Dicionário com a chave "Ola" e o valor "Mundo".
    """
    return {"Olá": "Mundo"}