import json
from pathlib import Path

class RepositorioJSON:
    def __init__(self, caminho="dados/publicacoes.json"):
        self.__caminho = Path(caminho)
        self.__caminho.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def salvar(self, dados):
        with self.__caminho.open(
            "w", encoding="utf-8"
        ) as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def listar(self):
        if not self.__caminho.exists():
            return []

        with self.__caminho.open(
            "r", encoding="utf-8"
        ) as arquivo:
            return json.load(arquivo)
