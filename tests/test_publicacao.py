import pytest

from publicacoes.publicacao import Publicacao
from publicacoes.status_leitura import StatusLeitura


@pytest.fixture
def publicacao():
    return Publicacao(
        1,
        "Harry Potter e a Pedra Filosofal",
        "J.K. Rowling",
        1997,
        "Fantasia",
        223,
        StatusLeitura.NAO_LIDO
    )

# TESTES DOS GETTERS

def test_get_id(publicacao):
    assert publicacao.get_id() == 1


def test_get_titulo(publicacao):
    assert publicacao.get_titulo() == "Harry Potter e a Pedra Filosofal"


def test_get_autor(publicacao):
    assert publicacao.get_autor() == "J.K. Rowling"


def test_get_ano(publicacao):
    assert publicacao.get_ano() == 1997


def test_get_genero(publicacao):
    assert publicacao.get_genero() == "Fantasia"


def test_get_numPaginas(publicacao):
    assert publicacao.get_numPaginas() == 223


def test_get_status(publicacao):
    assert publicacao.get_status() == StatusLeitura.NAO_LIDO


def test_get_avaliacao(publicacao):
    assert publicacao.get_avaliacao() is None


def test_get_dataInclusao(publicacao):
    assert publicacao.get_dataInclusao() is None

#TESTES DOS SETTERS

def test_set_titulo(publicacao):
    publicacao.set_titulo("Percy Jackson e o Ladrão de Raios")

    assert publicacao.get_titulo() == "Percy Jackson e o Ladrão de Raios"


def test_set_autor(publicacao):
    publicacao.set_autor("Rick Riordan")

    assert publicacao.get_autor() == "Rick Riordan"


def test_set_ano(publicacao):
    publicacao.set_ano(2005)

    assert publicacao.get_ano() == 2005


def test_set_genero(publicacao):
    publicacao.set_genero("Aventura")

    assert publicacao.get_genero() == "Aventura"


def test_set_numPaginas(publicacao):
    publicacao.set_numPaginas(400)

    assert publicacao.get_numPaginas() == 400


def test_set_status(publicacao):
    publicacao.set_status(StatusLeitura.LIDO)

    assert publicacao.get_status() == StatusLeitura.LIDO


def test_set_avaliacao(publicacao):
    publicacao.set_avaliacao(9.5)

    assert publicacao.get_avaliacao() == 9.5


#TESTES DE VALIDAÇÃO

def test_titulo_nao_pode_ser_vazio(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_titulo("")


def test_autor_nao_pode_ser_vazio(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_autor("")


def test_ano_deve_ser_maior_que_zero(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_ano(0)


def test_ano_deve_ser_inteiro(publicacao):
    with pytest.raises(TypeError):
        publicacao.set_ano("2000")


def test_genero_nao_pode_ser_vazio(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_genero("")


def test_numero_de_paginas_deve_ser_maior_que_zero(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_numPaginas(0)


def test_numero_de_paginas_deve_ser_inteiro(publicacao):
    with pytest.raises(TypeError):
        publicacao.set_numPaginas("300")


def test_avaliacao_deve_estar_entre_zero_e_dez(publicacao):
    with pytest.raises(ValueError):
        publicacao.set_avaliacao(11)


def test_avaliacao_deve_ser_numero(publicacao):
    with pytest.raises(TypeError):
        publicacao.set_avaliacao("muito bom")

# TESTES DOS MÉTODOS ESPECIAIS

def test_str(publicacao):
    assert str(publicacao) == (
        "Harry Potter e a Pedra Filosofal - J.K. Rowling"
    )


def test_repr(publicacao):
    resultado = repr(publicacao)

    assert "Publicacao" in resultado
    assert "Harry Potter e a Pedra Filosofal" in resultado
    assert "J.K. Rowling" in resultado


def test_igualdade(publicacao):
    outra_publicacao = Publicacao(
        1,
        "Outro Livro",
        "Outro Autor",
        2020,
        "Aventura",
        300,
        StatusLeitura.NAO_LIDO
    )

    assert publicacao == outra_publicacao


def test_publicacoes_diferentes(publicacao):
    outra_publicacao = Publicacao(
        2,
        "Jogos Vorazes",
        "Suzanne Collins",
        2008,
        "Distopia",
        400,
        StatusLeitura.NAO_LIDO
    )

    assert publicacao != outra_publicacao


def test_menor_que(publicacao):
    outra_publicacao = Publicacao(
        2,
        "Percy Jackson e o Ladrão de Raios",
        "Rick Riordan",
        2005,
        "Fantasia",
        400,
        StatusLeitura.NAO_LIDO
    )

    assert publicacao < outra_publicacao
