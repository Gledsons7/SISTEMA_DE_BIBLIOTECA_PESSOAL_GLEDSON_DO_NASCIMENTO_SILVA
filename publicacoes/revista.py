from publicacoes.publicacao import Publicacao


class Revista(Publicacao):
    """Representa uma revista ou periódico da biblioteca."""

    def __init__(
        self,
        id,
        titulo,
        autor,
        ano,
        genero,
        numPaginas,
        status,
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
            avaliacao,
            dataInclusao
        )

    def __str__(self):
        return f"Revista: {self.get_titulo()} - {self.get_autor()}"
