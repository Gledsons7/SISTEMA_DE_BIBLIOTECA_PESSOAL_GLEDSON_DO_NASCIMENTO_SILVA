class Colecao:
    def __init__(self, id, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        self.__id = id
        self.__nome = nome.strip()
        self.__publicacoes = []

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def adicionar_publicacao(self, publicacao):
        if publicacao not in self.__publicacoes:
            self.__publicacoes.append(publicacao)

    def remover_publicacao(self, publicacao):
        if publicacao in self.__publicacoes:
            self.__publicacoes.remove(publicacao)

    def listar_publicacoes(self):
        return self.__publicacoes.copy()

