from abc import ABC
from datetime import date


class Publicacao(ABC):
    """Representa uma publicação da biblioteca."""

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
        # Atributo privado
        self.__id = id

        # Os demais atributos são definidos através dos setters.
        # Dessa forma, as regras de validação são aplicadas.
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_ano(ano)
        self.set_genero(genero)
        self.set_numPaginas(numPaginas)
        self.set_status(status)
        self.set_avaliacao(avaliacao)
        self.set_dataInclusao(dataInclusao)

```python

@property
def id(self):
    return self.__id

@id.setter
def id(self, id):
    if id is None:
        raise ValueError("O ID não pode ser vazio.")

    self.__id = id

@property
def titulo(self):
    return self.__titulo

@titulo.setter
def titulo(self, titulo):
    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("O título não pode estar/ser vazio.")

    self.__titulo = titulo.strip()


@property
def autor(self):
    return self.__autor

@autor.setter
def autor(self, autor):
    if not isinstance(autor, str) or not autor.strip():
        raise ValueError("O autor não pode ser vazio.")

    self.__autor = autor.strip()


@property
def ano(self):
    return self.__ano

@ano.setter
def ano(self, ano):
    if not isinstance(ano, int):
        raise TypeError("O ano deve ser um número inteiro.")

    if ano <= 0:
        raise ValueError("O ano deve ser maior que zero.")

    self.__ano = ano


@property
def genero(self):
    return self.__genero

@genero.setter
def genero(self, genero):
    if not isinstance(genero, str) or not genero.strip():
        raise ValueError("O gênero não pode ser vazio.")

    self.__genero = genero.strip()


@property
def numPaginas(self):
    return self.__numPaginas

@numPaginas.setter
def numPaginas(self, numPaginas):
    if not isinstance(numPaginas, int):
        raise TypeError("O número de páginas deve ser um número inteiro.")

    if numPaginas <= 0:
        raise ValueError("O número de páginas deve ser maior que zero.")

    self.__numPaginas = numPaginas


@property
def status(self):
    return self.__status

@status.setter
def status(self, status):
    if status is None:
        raise ValueError("O status não pode ser vazio.")

    self.__status = status


@property
def avaliacao(self):
    return self.__avaliacao

@avaliacao.setter
def avaliacao(self, avaliacao):
    if avaliacao is not None:
        if not isinstance(avaliacao, (int, float)):
            raise TypeError("A avaliação deve ser um número.")

        if avaliacao < 0 or avaliacao > 10:
            raise ValueError(
                "A avaliação deve estar entre 0 e 10."
            )

    self.__avaliacao = avaliacao


@property
def dataInclusao(self):
    return self.__dataInclusao

@dataInclusao.setter
def dataInclusao(self, dataInclusao):
    if dataInclusao is not None and not isinstance(dataInclusao, date):
        raise TypeError(
            "A data de inclusão deve ser uma data válida."
        )

    self.__dataInclusao = dataInclusao
```

        
    # VALIDAÇÃO

    def validarDados(self):
        """Verifica se os dados da publicação são válidos."""

        if not self.__titulo:
            return False

        if not self.__autor:
            return False

        if self.__ano <= 0:
            return False

        if self.__numPaginas <= 0:
            return False

        if self.__avaliacao is not None:
            if self.__avaliacao < 0 or self.__avaliacao > 10:
                return False

        return True

    # MÉTODOS ESPECIAIS

    def __str__(self):
        return f"{self.__titulo} - {self.__autor}"

    def __repr__(self):
        return (
            f"Publicacao("
            f"id={self.__id}, "
            f"titulo='{self.__titulo}', "
            f"autor='{self.__autor}')"
        )

    def __eq__(self, outra):
        if not isinstance(outra, Publicacao):
            return False

        return self.__id == outra.get_id()

    def __lt__(self, outra):
        if not isinstance(outra, Publicacao):
            return NotImplemented

        return self.__titulo < outra.get_titulo()
