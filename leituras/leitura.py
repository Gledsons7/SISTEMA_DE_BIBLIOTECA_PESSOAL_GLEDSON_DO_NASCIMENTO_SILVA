from datetime import date

from publicacoes.status_leitura import StatusLeitura


class Leitura:
    """Representa o acompanhamento da leitura de uma publicação."""

    def __init__(
        self,
        data_inicio,
        data_fim=None,
        status=StatusLeitura.NAO_LIDO,
        progresso=0
    ):
        self.set_data_inicio(data_inicio)
        self.set_data_fim(data_fim)
        self.set_status(status)
        self.set_progresso(progresso)

    # GETTERS

    def get_data_inicio(self):
        return self.__data_inicio

    def get_data_fim(self):
        return self.__data_fim

    def get_status(self):
        return self.__status

    def get_progresso(self):
        return self.__progresso

    # SETTERS

    def set_data_inicio(self, data_inicio):
        if not isinstance(data_inicio, date):
            raise TypeError(
                "A data de início deve ser uma data válida."
            )

        self.__data_inicio = data_inicio

    def set_data_fim(self, data_fim):
        if data_fim is not None and not isinstance(data_fim, date):
            raise TypeError(
                "A data de fim deve ser uma data válida."
            )

        self.__data_fim = data_fim

    def set_status(self, status):
        if not isinstance(status, StatusLeitura):
            raise TypeError(
                "O status deve ser um valor de StatusLeitura."
            )

        self.__status = status

    def set_progresso(self, progresso):
        if not isinstance(progresso, (int, float)):
            raise TypeError(
                "O progresso deve ser um número."
            )

        if progresso < 0 or progresso > 100:
            raise ValueError(
                "O progresso deve estar entre 0 e 100."
            )

        self.__progresso = progresso

    # MÉTODOS

    def atualizar_progresso(self, progresso):
        self.set_progresso(progresso)

    # MÉTODO ESPECIAL

    def __str__(self):
        return (
            f"Status: {self.__status.name} | "
            f"Progresso: {self.__progresso}%"
        )
