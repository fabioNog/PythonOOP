from abc import ABC, abstractmethod

# Classe base abstrata Animal
class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

# Classe Mamifero que herda de Animal
class Mamifero(Animal):
    def emitir_som(self):
        print("Som de mamífero")

    def mamar(self):
        print("O mamífero está mamando")

# Classe Ave que herda de Animal
class Ave(Animal):
    def emitir_som(self):
        print("Som de ave")

    def voar(self):
        print("A ave está voando")

# Classe Morcego que herda de Mamifero e Ave (herança múltipla)
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        print("O morcego emite um som específico de morcego")

# Criando instâncias e utilizando os métodos

# Instância de Mamifero
mamifero = Mamifero()
mamifero.emitir_som()
mamifero.mamar()

# Instância de Ave
ave = Ave()
ave.emitir_som()
ave.voar()

# Instância de Morcego
morcego = Morcego()
morcego.emitir_som()
morcego.mamar()
morcego.voar()
