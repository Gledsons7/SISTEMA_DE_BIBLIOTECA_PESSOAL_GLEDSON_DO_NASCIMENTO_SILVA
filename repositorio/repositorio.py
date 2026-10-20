from abc import ABC, abstractmethod


class Repositorio(ABC):
    """Interface com as operações básicas de persistência."""

    @abstractmethod
    def salvar(self, dados):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def remover(self, id):
        pass
