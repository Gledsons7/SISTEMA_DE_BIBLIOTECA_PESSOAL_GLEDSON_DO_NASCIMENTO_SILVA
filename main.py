
from repositorio.repositorio_json import RepositorioJSON
from publicacoes.livro import Livro
from publicacoes.revista import Revista
from publicacoes.livro_digital import LivroDigital
from publicacoes.status_leitura import StatusLeitura

repo = RepositorioJSON()


def carregar():
    return repo.listar()


def salvar(dados):
    repo.salvar(dados)


def listar(dados=None):
    dados = carregar() if dados is None else dados

    if not dados:
        print("Nenhuma publicação cadastrada.")
        return

    for p in dados:
        print(
            f"ID: {p['id']} | {p.get('tipo', 'Publicação')} | "
            f"{p['titulo']} | {p['autor']} | "
            f"{p['status']}"
        )


def cadastrar():
    try:
        dados = carregar()
        id = max((int(p["id"]) for p in dados), default=0) + 1

        print("\nTipos: livro, revista, digital")
        tipo = input("Tipo: ").strip().lower()
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = int(input("Ano: "))
        genero = input("Gênero: ").strip()
        paginas = int(input("Número de páginas: "))

        print("Status: NAO_LIDO, LENDO ou LIDO")
        status = StatusLeitura[
            input("Status: ").strip().upper()
        ]

        nota = input("Avaliação (0 a 10, opcional): ").strip()
        avaliacao = float(nota) if nota else None

        if tipo == "livro":
            objeto = Livro(
                id, titulo, autor, ano, genero,
                paginas, status, avaliacao
            )
        elif tipo == "revista":
            objeto = Revista(
                id, titulo, autor, ano, genero,
                paginas, status, avaliacao
            )
        elif tipo == "digital":
            formato = input("Formato (PDF, EPUB etc.): ").strip()
            tamanho = float(input("Tamanho em MB: "))
            objeto = LivroDigital(
                id, titulo, autor, ano, genero, paginas,
                status, formato, tamanho, avaliacao
            )
        else:
            print("Tipo inválido.")
            return

        # A criação do objeto aplica as validações da classe.
        if not objeto.validarDados():
            print("Os dados da publicação são inválidos.")
            return

        dados.append({
            "id": id,
            "tipo": tipo,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero,
            "numPaginas": paginas,
            "status": status.name,
            "avaliacao": avaliacao,
            **(
                {"formato": formato, "tamanhoMB": tamanho}
                if tipo == "digital" else {}
            )
        })

        salvar(dados)
        print(f"Publicação cadastrada! ID: {id}")

    except (ValueError, TypeError, KeyError) as erro:
        print(f"Não foi possível cadastrar: {erro}")


def buscar(id):
    for p in carregar():
        if str(p["id"]) == id:
            for chave, valor in p.items():
                print(f"{chave}: {valor}")
            return
    print("Publicação não encontrada.")


def remover(id):
    dados = carregar()
    novos = [p for p in dados if str(p["id"]) != id]

    if len(novos) == len(dados):
        print("Publicação não encontrada.")
    else:
        salvar(novos)
        print("Publicação removida!")


def filtrar(campo, valor):
    dados = carregar()

    if campo == "status":
        valor = valor.upper()
    elif campo == "genero":
        valor = valor.lower()

    resultado = [
        p for p in dados
        if str(p.get(campo, "")).lower() == valor.lower()
    ]
    listar(resultado)


def relatorio():
    dados = carregar()

    if not dados:
        print("Não há dados para gerar o relatório.")
        return

    print("\n=== RELATÓRIO DA BIBLIOTECA ===")
    print(f"Total de publicações: {len(dados)}")

    for tipo in ("livro", "revista", "digital"):
        total = sum(1 for p in dados if p.get("tipo") == tipo)
        print(f"{tipo.capitalize()}s: {total}")

    for status in StatusLeitura:
        total = sum(1 for p in dados if p["status"] == status.name)
        percentual = total / len(dados) * 100
        print(f"{status.name}: {total} ({percentual:.1f}%)")

    notas = [
        float(p["avaliacao"]) for p in dados
        if p.get("avaliacao") is not None
    ]

    if notas:
        print(f"Média das avaliações: {sum(notas) / len(notas):.2f}")

    print("\nPublicações mais bem avaliadas:")
    avaliadas = sorted(
        (p for p in dados if p.get("avaliacao") is not None),
        key=lambda p: float(p["avaliacao"]),
        reverse=True
    )

    for p in avaliadas[:5]:
        print(f"- {p['titulo']}: {p['avaliacao']}/10")


def ajuda():
    print("""
=== COMANDOS DA BIBLIOTECA ===
ajuda                  Mostra os comandos
cadastrar              Cadastra uma publicação
listar                 Lista as publicações
buscar ID              Busca pelo ID
remover ID             Remove pelo ID
filtrar status STATUS  Filtra por status
filtrar genero NOME    Filtra por gênero
ordenar titulo         Ordena por título
relatorio              Exibe estatísticas
sair                   Encerra o sistema
""")


def executar():
    print("=== SISTEMA DE BIBLIOTECA PESSOAL ===")
    print("Digite 'ajuda' para ver os comandos.")

    while True:
        try:
            comando = input("\nbiblioteca> ").strip()
            partes = comando.split(maxsplit=2)

            if not partes:
                continue

            acao = partes[0].lower()

            if acao == "ajuda":
                ajuda()
            elif acao == "cadastrar":
                cadastrar()
            elif acao == "listar":
                listar()
            elif acao == "buscar" and len(partes) == 2:
                buscar(partes[1])
            elif acao == "remover" and len(partes) == 2:
                remover(partes[1])
            elif acao == "filtrar" and len(partes) == 3:
                campo = partes[1].lower()
                if campo in ("status", "genero"):
                    filtrar(campo, partes[2])
                else:
                    print("Use status ou genero.")
            elif acao == "ordenar" and len(partes) == 2:
                if partes[1].lower() == "titulo":
                    listar(sorted(
                        carregar(),
                        key=lambda p: p["titulo"].lower()
                    ))
                else:
                    print("Ordenação disponível: titulo.")
            elif acao == "relatorio":
                relatorio()
            elif acao == "sair":
                print("Sistema encerrado.")
                break
            else:
                print("Comando inválido. Digite 'ajuda'.")

        except (EOFError, KeyboardInterrupt):
            print("\nSistema encerrado.")
            break
        except (ValueError, TypeError, KeyError) as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    executar()

