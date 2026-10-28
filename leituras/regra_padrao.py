from leituras.regra_leitura import RegraLeitura


class RegraPadrao(RegraLeitura):
    def __init__(self):
        super().__init__("Regra padrão")

    def validar_progresso(self, progresso):
        if not isinstance(progresso, (int, float)) or isinstance(progresso, bool):
            raise TypeError("O progresso deve ser numérico.")
        if not 0 <= progresso <= 100:
            raise ValueError("O progresso deve estar entre 0 e 100.")
        return True
