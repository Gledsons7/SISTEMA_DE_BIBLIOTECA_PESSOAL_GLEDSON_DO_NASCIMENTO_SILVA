from publicacoes.publicacao_digital import PublicacaoDigital


class LivroDigital(PublicacaoDigital):
    """Representa um livro digital da biblioteca."""

    def __init__(
        self,
        id,
        titulo,
        autor,
        ano,
        genero,
        numPaginas,
        status,
        formato,
        tamanhoMB,
        avaliacao=None,
        dataInclusao=None
    ):
        super().__init__(
            id,
            titulo,
            autor,
            ano,
            genero,
            numPaginas,
            status,
            formato,
            tamanhoMB,
            avaliacao,
            dataInclusao
        )

    def __str__(self):
        return (
            f"Livro digital: {self.get_titulo()} - "
            f"{self.get_autor()} - "
            f"Formato: {self.get_formato()}"
        )
