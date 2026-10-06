class Usuario:
    """Representa o usuário da biblioteca."""

    def __init__(self, nome, email, senha):
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)

    # GETTERS

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    # SETTERS

    def set_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        self.__nome = nome.strip()

    def set_email(self, email):
        if not isinstance(email, str) or not email.strip():
            raise ValueError("O e-mail não pode ser vazio.")

        self.__email = email.strip()

    def set_senha(self, senha):
        if not isinstance(senha, str) or not senha:
            raise ValueError("A senha não pode ser vazia.")

        self.__senha = senha

    # MÉTODOS ESPECIAIS

    def __str__(self):
        return f"Usuário: {self.__nome} - {self.__email}"

    def __repr__(self):
        return f"Usuario(nome='{self.__nome}', email='{self.__email}')"

    def __eq__(self, outro):
        if not isinstance(outro, Usuario):
            return False

        return self.__email == outro.get_email()
