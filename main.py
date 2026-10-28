from repositorio.repositorio_json import RepositorioJSON
from publicacoes.livro import Livro
from publicacoes.revista import Revista
from publicacoes.livro_digital import LivroDigital
from publicacoes.status_leitura import StatusLeitura
from repositorio.repositorio_colecoes import RepositorioColecoes
from relatorios.relatorio import Relatorio

repo = RepositorioJSON()
repo_colecoes = RepositorioColecoes()

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

    Relatorio(dados).gerar()

    notas = [float(p["avaliacao"]) for p in dados
             if p.get("avaliacao") is not None]

    avaliadas = sorted(
        [p for p in dados if p.get("avaliacao") is not None],
        key=lambda p: float(p["avaliacao"]), reverse=True
    )

    print("\nPublicações mais bem avaliadas:")
    for p in avaliadas[:5]:
        print(f'- {p["titulo"]}: {p["avaliacao"]}/10')


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
colecao criar NOME     Cria uma coleção
colecao listar         Lista as coleções
colecao ver ID         Mostra uma coleção
""")


def executar():
    print("=== SISTEMA DE BIBLIOTECA PESSOAL ===")
    print("Digite 'ajuda' para ver os comandos.")

    while True:
        try:
            comando = input("\nbiblioteca> ").strip()
            partes = comando.split()

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
            elif acao == "colecao" and len(partes) >= 2:
                opcao = partes[1].lower()

                if opcao == "criar" and len(partes) == 3:
                    criar_colecao(partes[2])
                elif opcao == "listar":
                    listar_colecoes()

                elif opcao == "adicionar" and len(partes) == 3:
                    ids = partes[2].split()
                    print("Use: colecao adicionar ID_COLECAO ID_PUBLICACAO")

                elif opcao == "adicionar" and len(partes) == 4:
                    adicionar_colecao(int(partes[2]), int(partes[3]))

                elif opcao == "remover" and len(partes) == 4:
                    remover_colecao(int(partes[2]), int(partes[3]))
                
                elif opcao == "ver" and len(partes) == 3:
                    ver_colecao(int(partes[2]))
                else:
                    print("Comando de colecao invalido.")
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


def criar_colecao(nome):
    colecoes = repo_colecoes.listar()
    id = max([c["id"] for c in colecoes], default=0) + 1
    colecoes.append({"id": id, "nome": nome, "publicacoes": []})
    repo_colecoes.salvar(colecoes)
    print(f"Coleção '{nome}' criada!")


def listar_colecoes():
    for c in repo_colecoes.listar():
        print(f'{c["id"]} - {c["nome"]}')


def ver_colecao(id):
    for c in repo_colecoes.listar():
        if c["id"] == id:
            print(c["nome"])
            for id_pub in c["publicacoes"]:
                p = next((p for p in carregar()
                          if str(p["id"]) == str(id_pub)), None)
                if p:
                    print("-", p["titulo"])
            return
    print("Coleção não encontrada.")

def adicionar_colecao(id_colecao, id_publicacao):
    colecoes = repo_colecoes.listar()
    publicacoes = carregar()

    colecao = next((c for c in colecoes if c["id"] == id_colecao), None)
    publicacao = next((p for p in publicacoes if str(p["id"]) == str(id_publicacao)), None)

    if not colecao:
        print("Coleção não encontrada.")
    elif not publicacao:
        print("Publicação não encontrada.")
    elif id_publicacao in colecao["publicacoes"]:
        print("Publicação já está na coleção.")
    else:
        colecao["publicacoes"].append(id_publicacao)
        repo_colecoes.salvar(colecoes)
        print("Publicação adicionada à coleção!")

def remover_colecao(id_colecao, id_publicacao):
    colecoes = repo_colecoes.listar()

    for c in colecoes:
        if c["id"] == id_colecao:
            if id_publicacao in c["publicacoes"]:
                c["publicacoes"].remove(id_publicacao)
                repo_colecoes.salvar(colecoes)
                print("Publicação removida da coleção!")
            else:
                print("Publicação não está na coleção.")
            return

    print("Coleção não encontrada.")

if __name__ == "__main__":
    executar()