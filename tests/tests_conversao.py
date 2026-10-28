def test_to_dict_livro():
    livro = Livro(
        1, "A Cinco Passos de Você", "Rachael Lippincott", 2018,
        "Romance", 288, StatusLeitura.LIDO, 9.5, date(2026, 10, 1)
    )

    dados = livro.to_dict()

    assert dados["tipo"] == "Livro"
    assert dados["titulo"] == "A Cinco Passos de Você"
    assert dados["status"] == "LIDO"
    assert dados["dataInclusao"] == "2026-10-01"


def test_from_dict_livro():
    livro = Livro(
        1, "A Cinco Passos de Você", "Rachael Lippincott", 2018,
        "Romance", 288, StatusLeitura.LENDO, 8, date(2026, 10, 1)
    )

    copia = Livro.from_dict(livro.to_dict())

    assert copia == livro
    assert copia.get_titulo() == "A Cinco Passos de Você"
    assert copia.get_status() == StatusLeitura.LENDO
    assert copia.get_dataInclusao() == date(2026, 10, 1)
