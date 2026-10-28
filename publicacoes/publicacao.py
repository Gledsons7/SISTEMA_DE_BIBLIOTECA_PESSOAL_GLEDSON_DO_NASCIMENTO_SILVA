
from abc import ABC
from datetime import date
from publicacoes.status_leitura import StatusLeitura


class Publicacao(ABC):
    """Representa uma publicação da biblioteca."""

    def __init__(self, id, titulo, autor, ano, genero,
                 numPaginas, status, avaliacao=None,
                 dataInclusao=None):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_ano(ano)
        self.set_genero(genero)
        self.set_numPaginas(numPaginas)
        self.set_status(status)
        self.set_avaliacao(avaliacao)
        self.set_dataInclusao(dataInclusao)

    # GETTERS
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_genero(self):
        return self.__genero

    def get_numPaginas(self):
        return self.__numPaginas

    def get_status(self):
        return self.__status

    def get_avaliacao(self):
        return self.__avaliacao

    def get_dataInclusao(self):
        return self.__dataInclusao

    # SETTERS
    def set_id(self, id):
        if id is None:
            raise ValueError("O ID não pode ser vazio.")
        self.__id = id

    def set_titulo(self, titulo):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("O título não pode ser vazio.")
        self.__titulo = titulo.strip()

    def set_autor(self, autor):
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("O autor não pode ser vazio.")
        self.__autor = autor.strip()

    def set_ano(self, ano):
        if not isinstance(ano, int) or isinstance(ano, bool):
            raise TypeError("O ano deve ser um número inteiro.")
        if ano <= 0:
            raise ValueError("O ano deve ser maior que zero.")
        self.__ano = ano

    def set_genero(self, genero):
        if not isinstance(genero, str) or not genero.strip():
            raise ValueError("O gênero não pode ser vazio.")
        self.__genero = genero.strip()

    def set_numPaginas(self, numPaginas):
        if not isinstance(numPaginas, int) or isinstance(numPaginas, bool):
            raise TypeError("O número de páginas deve ser um inteiro.")
        if numPaginas <= 0:
            raise ValueError("O número de páginas deve ser positivo.")
        self.__numPaginas = numPaginas

    def set_status(self, status):
        if not isinstance(status, StatusLeitura):
            raise ValueError("Status inválido.")
        self.__status = status

    def set_avaliacao(self, avaliacao):
        if avaliacao is not None:
            if not isinstance(avaliacao, (int, float)) or isinstance(avaliacao, bool):
                raise TypeError("A avaliação deve ser um número.")
            if not 0 <= avaliacao <= 10:
                raise ValueError("A avaliação deve estar entre 0 e 10.")
        self.__avaliacao = avaliacao

    def set_dataInclusao(self, dataInclusao):
        if dataInclusao is not None and not isinstance(dataInclusao, date):
            raise TypeError("A data de inclusão deve ser válida.")
        self.__dataInclusao = dataInclusao

    # CONVERSÃO PARA DICIONÁRIO
    def to_dict(self):
        data = self.get_dataInclusao()
        return {
            "tipo": type(self).__name__,
            "id": self.get_id(),
            "titulo": self.get_titulo(),
            "autor": self.get_autor(),
            "ano": self.get_ano(),
            "genero": self.get_genero(),
            "numPaginas": self.get_numPaginas(),
            "status": self.get_status().name,
            "avaliacao": self.get_avaliacao(),
            "dataInclusao": data.isoformat() if data else None
        }

    @classmethod
    def from_dict(cls, dados):
        data = dados.get("dataInclusao")
        if data:
            data = date.fromisoformat(data)

        return cls(
            dados["id"], dados["titulo"], dados["autor"],
            dados["ano"], dados["genero"], dados["numPaginas"],
            StatusLeitura[dados["status"]],
            dados.get("avaliacao"), data
        )

    def validarDados(self):
        return (
            bool(self.__titulo)
            and bool(self.__autor)
            and self.__ano > 0
            and self.__numPaginas > 0
            and (
                self.__avaliacao is None
                or 0 <= self.__avaliacao <= 10
            )
        )

    # MÉTODOS ESPECIAIS
    def __str__(self):
        return f"{self.__titulo} - {self.__autor}"

    def __repr__(self):
        return (
            f"Publicacao(id={self.__id}, "
            f"titulo='{self.__titulo}', autor='{self.__autor}')"
        )

    def __eq__(self, outra):
        if not isinstance(outra, Publicacao):
            return False
        return self.__id == outra.get_id()

    def __lt__(self, outra):
        if not isinstance(outra, Publicacao):
            return NotImplemented
        return self.__titulo < outra.get_titulo()
