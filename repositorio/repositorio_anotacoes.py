
import json
from pathlib import Path


class RepositorioAnotacoes:
    def __init__(self, caminho="dados/anotacoes.json"):
        self.caminho = Path(caminho)
        self.caminho.parent.mkdir(parents=True, exist_ok=True)

    def listar(self):
        if not self.caminho.exists():
            return []
        return json.loads(self.caminho.read_text(encoding="utf-8"))

    def salvar(self, dados):
        self.caminho.write_text(
            json.dumps(dados, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )
