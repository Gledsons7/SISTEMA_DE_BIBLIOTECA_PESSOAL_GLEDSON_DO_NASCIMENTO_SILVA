from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from publicacoes.status_leitura import StatusLeitura


class Publicacao(ABC):
    """Classe abstrata que representa uma publicação."""

    def __init__(
        self,
        id,
        titulo,
        autor,
        ano,
        genero,
        numPaginas,
        status,
        avaliacao=None,
        dataInclusao=None
    ):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__genero = genero
        self.__numPaginas = numPaginas
        self.__status = status
        self.__avaliacao = avaliacao
        self.__dataInclusao = dataInclusao

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
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ano(self, ano):
        self.__ano = ano

    def set_genero(self, genero):
        self.__genero = genero

    def set_numPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def set_status(self, status):
        self.__status = status

    def set_avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    def set_dataInclusao(self, dataInclusao):
        self.__dataInclusao = dataInclusao

    # MÉTODOS ESPECIAIS

    def __str__(self):
        return f"{self.__titulo} - {self.__autor}"

    def __repr__(self):
        return f"Publicacao(id={self.__id}, titulo='{self.__titulo}', autor='{self.__autor}')"

    def __eq__(self, outra):
        if not isinstance(outra, Publicacao):
            return False

        return self.__id == outra.get_id()

    def __lt__(self, outra):
        if not isinstance(outra, Publicacao):
            return NotImplemented

        return self.__titulo < outra.get_titulo()

    # OUTROS MÉTODOS DA UML

    def validarDados(self):
        if not self.__titulo:
            return False

        if not self.__autor:
            return False

        if self.__ano <= 0:
            return False

        if self.__numPaginas <= 0:
            return False

        return True

    def atualizarStatus(self, status):
        self.__status = status
