import pytest

from repositorio.repositorio import Repositorio
from repositorio.repositorio_json import RepositorioJSON


def test_interface_nao_pode_ser_instanciada():
    with pytest.raises(TypeError):
        Repositorio()


def test_json_salva_e_lista(tmp_path):
    caminho = tmp_path / "publicacoes.json"
    repositorio = RepositorioJSON(str(caminho))

    repositorio.salvar([{"id": 1, "titulo": "Dom Casmurro"}])

    assert repositorio.listar() == [{"id": 1, "titulo": "Dom Casmurro"}]


def test_json_lista_vazio_se_arquivo_nao_existe(tmp_path):
    caminho = tmp_path / "nao_existe.json"
    repositorio = RepositorioJSON(str(caminho))

    assert repositorio.listar() == []
