class Configuracao:
    """Representa as configurações personalizadas do usuário."""

    def __init__(
        self,
        genero_favorito,
        limite_leituras_simultaneas,
        meta_anual
    ):
        self.set_genero_favorito(genero_favorito)
        self.set_limite_leituras_simultaneas(
            limite_leituras_simultaneas
        )
        self.set_meta_anual(meta_anual)

    # GETTERS

    def get_genero_favorito(self):
        return self.__genero_favorito

    def get_limite_leituras_simultaneas(self):
        return self.__limite_leituras_simultaneas

    def get_meta_anual(self):
        return self.__meta_anual

    # SETTERS

    def set_genero_favorito(self, genero_favorito):
        if not isinstance(genero_favorito, str) or not genero_favorito.strip():
            raise ValueError("O gênero favorito não pode ser vazio.")

        self.__genero_favorito = genero_favorito.strip()

    def set_limite_leituras_simultaneas(self, limite):
        if not isinstance(limite, int):
            raise TypeError(
                "O limite de leituras deve ser um número inteiro."
            )

        if limite < 0:
            raise ValueError(
                "O limite de leituras não pode ser negativo."
            )

        self.__limite_leituras_simultaneas = limite

    def set_meta_anual(self, meta_anual):
        if not isinstance(meta_anual, int):
            raise TypeError(
                "A meta anual deve ser um número inteiro."
            )

        if meta_anual < 0:
            raise ValueError(
                "A meta anual não pode ser negativa."
            )

        self.__meta_anual = meta_anual

    # MÉTODO ESPECIAL

    def __str__(self):
        return (
            f"Gênero favorito: {self.__genero_favorito} | "
            f"Limite de leituras: "
            f"{self.__limite_leituras_simultaneas} | "
            f"Meta anual: {self.__meta_anual}"
        )
