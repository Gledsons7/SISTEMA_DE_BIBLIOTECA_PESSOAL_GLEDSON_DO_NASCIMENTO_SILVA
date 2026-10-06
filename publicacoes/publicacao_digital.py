from publicacoes.publicacao import Publicacao


class PublicacaoDigital(Publicacao):
    """Classe base das publicações digitais."""

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato

    def __str__(self):
        return f"{super().__str__()} - Formato: {self.__formato}"
