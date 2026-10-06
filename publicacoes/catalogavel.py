from abc import ABC, abstractmethod


class Catalogavel(ABC):
    """Interface para operações de catalogação de publicações."""

    @abstractmethod
    def buscar_por_titulo(self, titulo):
        pass

    @abstractmethod
    def buscar_por_autor(self, autor):
        pass

    @abstractmethod
    def buscar_por_genero(self, genero):
        pass

    @abstractmethod
    def filtrar_por_status(self, status):
        pass
