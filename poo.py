class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Alice",30)

print("Nome: ", pessoa1.nome)
print("Idade: ", pessoa1.idade)