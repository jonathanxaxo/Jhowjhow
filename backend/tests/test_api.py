import os
os.environ["TESTING"] = "1"
from fastapi.testclient import TestClient
from app.database import Base, engine
from app.main import app

client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_crud_e_indicadores():
    payload = {"nome":"Horta Comunitária","unidade":"Unidade Verde","impacto_estimado":"Redução de resíduos orgânicos","progresso":25}
    criado = client.post("/api/iniciativas", json=payload)
    assert criado.status_code == 201
    item_id = criado.json()["id"]
    assert client.get("/api/iniciativas").json()[0]["nome"] == "Horta Comunitária"
    payload["progresso"] = 100
    assert client.put(f"/api/iniciativas/{item_id}", json=payload).status_code == 200
    assert client.get("/api/indicadores").json() == {"iniciativas":1,"finalizadas":1,"progresso_medio":100.0}
    assert client.delete(f"/api/iniciativas/{item_id}").status_code == 204


def test_validacao_de_progresso():
    payload = {"nome":"Teste inválido","unidade":"UV","impacto_estimado":"Impacto fictício","progresso":101}
    assert client.post("/api/iniciativas", json=payload).status_code == 422


def test_lista_vazia():
    assert client.get("/api/iniciativas").json() == []
    assert client.get("/api/indicadores").json()["iniciativas"] == 0
