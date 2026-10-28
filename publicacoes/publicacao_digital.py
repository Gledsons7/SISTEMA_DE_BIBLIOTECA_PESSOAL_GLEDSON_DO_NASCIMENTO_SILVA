from datetime import date
from publicacoes.publicacao import Publicacao
from publicacoes.status_leitura import StatusLeitura


class PublicacaoDigital(Publicacao):
    def __init__(
        self, id, titulo, autor, ano, genero, numPaginas,
        status, formato, tamanhoMB, avaliacao=None,
        dataInclusao=None
    ):
        super().__init__(
            id, titulo, autor, ano, genero, numPaginas,
            status, avaliacao, dataInclusao
        )
        self.set_formato(formato)
        self.set_tamanhoMB(tamanhoMB)

    def get_formato(self):
        return self.__formato

    def get_tamanhoMB(self):
        return self.__tamanhoMB

    def set_formato(self, formato):
        if not isinstance(formato, str) or not formato.strip():
            raise ValueError("O formato não pode ser vazio.")
        self.__formato = formato.strip()

    def set_tamanhoMB(self, tamanhoMB):
        if not isinstance(tamanhoMB, (int, float)) or isinstance(tamanhoMB, bool):
            raise TypeError("O tamanho deve ser numérico.")
        if tamanhoMB <= 0:
            raise ValueError("O tamanho deve ser maior que zero.")
        self.__tamanhoMB = tamanhoMB

    def baixar(self):
        return f"Baixando a publicação: {self.get_titulo()}"

    def abrir(self):
        return f"Abrindo a publicação: {self.get_titulo()}"

    def to_dict(self):
        dados = super().to_dict()
        dados["formato"] = self.get_formato()
        dados["tamanhoMB"] = self.get_tamanhoMB()
        return dados

    @classmethod
    def from_dict(cls, dados):
        data = dados.get("dataInclusao")
        if data is not None:
            data = date.fromisoformat(data)

        return cls(
            dados["id"], dados["titulo"], dados["autor"],
            dados["ano"], dados["genero"], dados["numPaginas"],
            StatusLeitura[dados["status"]],
            dados["formato"], dados["tamanhoMB"],
            dados.get("avaliacao"), data
        )

    def __str__(self):
        return (
            f"{self.get_titulo()} - {self.get_autor()} "
            f"- Formato: {self.get_formato()}"
        )
