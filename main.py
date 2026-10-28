def ajuda():
    print("""
Comandos disponíveis:
  ajuda       - Mostra os comandos
  listar      - Lista publicações
  cadastrar   - Cadastra uma publicação
  relatorio   - Mostra o relatório
  sair        - Encerra o programa
""")

print("=== MINHA BIBLIOTECA ===")
print("Digite 'ajuda' para ver os comandos.")

while True:
    comando = input("\nbiblioteca> ").strip().lower()

    if comando == "ajuda":
        ajuda()
    elif comando == "listar":
        print("Lista de publicações.")
    elif comando == "cadastrar":
        print("Cadastro de publicação.")
    elif comando == "relatorio":
        print("Relatório da biblioteca.")
    elif comando == "sair":
        print("Programa encerrado!")
        break
    else:
        print("Comando desconhecido. Digite 'ajuda'.")

