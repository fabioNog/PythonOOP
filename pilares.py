# Exemplo Herança
print("\n Exemplo de Herança")

class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome

        def andar(self):
            print("O Animal {self.nome} andou")
            return
        
        def emitir_som(self):
            pass

class Cachorro(Animal):
    def emitir_som(self):
        return "au,au"
    
class Gato(Animal):
    def emitir_som(self):
        return "miau"
    
dog = Cachorro(nome='Rex')
cat = Gato(nome='Felix')

animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

