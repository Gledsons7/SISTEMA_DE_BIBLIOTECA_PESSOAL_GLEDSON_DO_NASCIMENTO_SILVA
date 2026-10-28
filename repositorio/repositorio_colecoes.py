import json
from pathlib import Path

class RepositorioColecoes:
    def __init__(self):
        self.__caminho = Path("dados/colecoes.json")
        self.__caminho.parent.mkdir(parents=True, exist_ok=True)

    def listar(self):
        if not self.__caminho.exists():
            return []
        return json.loads(self.__caminho.read_text(encoding="utf-8"))

    def salvar(self, colecoes):
        self.__caminho.write_text(
            json.dumps(colecoes, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )