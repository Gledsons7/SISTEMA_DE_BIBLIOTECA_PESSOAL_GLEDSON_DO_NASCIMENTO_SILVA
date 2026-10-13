class Colecao:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__publicacoes = []

    def adicionar_publicacao(self, publicacao):
        if publicacao not in self.__publicacoes:
            self.__publicacoes.append(publicacao)

    def remover_publicacao(self, publicacao):
        if publicacao in self.__publicacoes:
            self.__publicacoes.remove(publicacao)

    def listar_publicacoes(self):
        return self.__publicacoes.copy()
