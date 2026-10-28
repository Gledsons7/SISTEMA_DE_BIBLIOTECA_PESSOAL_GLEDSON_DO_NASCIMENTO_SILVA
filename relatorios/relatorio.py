from publicacoes.status_leitura import StatusLeitura


class Relatorio:
    def __init__(self, publicacoes):
        self.publicacoes = publicacoes

    def gerar(self):
        pubs = self.publicacoes

        print("\n=== RELATÓRIO DA BIBLIOTECA ===")
        print("Total:", len(pubs))

        print("\nPor tipo:")
        for tipo in set(p["tipo"] for p in pubs):
            print(tipo, ":", sum(p["tipo"] == tipo for p in pubs))

        print("\nPor status:")
        for status in StatusLeitura:
            qtd = sum(p["status"] == status.name for p in pubs)
            print(status.name, ":", qtd)

        notas = [p["avaliacao"] for p in pubs if p["avaliacao"] is not None]
        media = sum(notas) / len(notas) if notas else 0
        print("\nMédia das avaliações:", round(media, 2))

        print("\nTítulos:")
        for p in pubs:
            print("-", p["titulo"])
