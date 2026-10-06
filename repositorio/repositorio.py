class Repositorio:
    """Classe base dos repositórios da biblioteca."""

    def __init__(self):
        self.__dados = []

    def get_dados(self):
        return self.__dados

    def adicionar(self, dado):
        self.__dados.append(dado)

    def remover(self, dado):
        if dado in self.__dados:
            self.__dados.remove(dado)

    def __len__(self):
        return len(self.__dados)

    def __str__(self):
        return f"Repositório com {len(self.__dados)} item(ns)"
