import json
import os

ARQUIVO = "data/banco.json"


def inicializar_banco():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(ARQUIVO):
        dados = {
            "pacientes": [],
            "medicos": [],
            "consultas": []
        }

        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)