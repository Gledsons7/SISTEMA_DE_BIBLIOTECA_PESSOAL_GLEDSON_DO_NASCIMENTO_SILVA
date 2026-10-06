class RegraLeitura:
    """Classe base das regras de leitura."""

    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f"Regra de leitura: {self.__nome}"
