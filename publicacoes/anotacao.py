from datetime import date


class Anotacao:
    """Representa uma anotação feita pelo usuário."""

    def __init__(self, texto, data, trecho=None):
        self.set_texto(texto)
        self.set_data(data)
        self.set_trecho(trecho)

    # GETTERS

    def get_texto(self):
        return self.__texto

    def get_data(self):
        return self.__data

    def get_trecho(self):
        return self.__trecho

    # SETTERS

    def set_texto(self, texto):
        if not isinstance(texto, str) or not texto.strip():
            raise ValueError("O texto da anotação não pode ser vazio.")

        self.__texto = texto.strip()

    def set_data(self, data):
        if not isinstance(data, date):
            raise TypeError("A data da anotação deve ser uma data válida.")

        self.__data = data

    def set_trecho(self, trecho):
        if trecho is not None and not isinstance(trecho, str):
            raise TypeError("O trecho deve ser um texto.")

        self.__trecho = trecho

    # MÉTODOS

    def editar(self, novo_texto):
        self.set_texto(novo_texto)

    def excluir(self):
        self.__texto = None
        self.__trecho = None

    # MÉTODO ESPECIAL

    def __str__(self):
        return self.__texto if self.__texto is not None else "Anotação excluída"
