from publicacoes.publicacao import Publicacao
from datetime import date
from publicacoes.status_leitura import StatusLeitura

class PublicacaoDigital(Publicacao):
    """Classe abstrata que representa uma publicação digital."""

    def __init__(
        self,
        id,
        titulo,
        autor,
        ano,
        genero,
        numPaginas,
        status,
        formato,
        tamanhoMB,
        avaliacao=None,
        dataInclusao=None
    ):
        super().__init__(
            id,
            titulo,
            autor,
            ano,
            genero,
            numPaginas,
            status,
            avaliacao,
            dataInclusao
        )

        self.__formato = formato
        self.__tamanhoMB = tamanhoMB

    # GETTERS

    def get_formato(self):
        return self.__formato

    def get_tamanhoMB(self):
        return self.__tamanhoMB

    # SETTERS

    def set_formato(self, formato):
        self.__formato = formato

    def set_tamanhoMB(self, tamanhoMB):
        self.__tamanhoMB = tamanhoMB

    # MÉTODOS DA UML

    def baixar(self):
        return f"Baixando a publicação: {self.get_titulo()}"

    def abrir(self):
        return f"Abrindo a publicação: {self.get_titulo()}"


    # CONVERSÃO PARA DICIONÁRIO

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
            dados["formato"],
            dados["tamanhoMB"],
            dados.get("avaliacao"),
            data
        )
    # MÉTODO ESPECIAL

    def __str__(self):
        return (
            f"{self.get_titulo()} - {self.get_autor()} "
            f"- Formato: {self.__formato}"
        )
