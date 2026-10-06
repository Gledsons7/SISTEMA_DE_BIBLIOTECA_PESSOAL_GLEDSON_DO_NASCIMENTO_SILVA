from publicacoes.publicacao import Publicacao


def test_get_titulo():
    publicacao = Publicacao("Dom Casmurro", "Machado de Assis")

    assert publicacao.get_titulo() == "Dom Casmurro"


def test_set_titulo():
    publicacao = Publicacao("Dom Casmurro", "Machado de Assis")

    publicacao.set_titulo("Memórias Póstumas")

    assert publicacao.get_titulo() == "Memórias Póstumas"


def test_get_autor():
    publicacao = Publicacao("Dom Casmurro", "Machado de Assis")

    assert publicacao.get_autor() == "Machado de Assis"


def test_str():
    publicacao = Publicacao("Dom Casmurro", "Machado de Assis")

    assert str(publicacao) == "Dom Casmurro"
