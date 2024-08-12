from abc import ABC, abstractmethod

# Classe abstrata Personagem
class Personagem(ABC):
    def __init__(self, nome, vida, nivel) -> None:
        if vida <= 0:
            raise ValueError("A vida deve ser maior que 0")
        if nivel <= 0:
            raise ValueError("O nível deve ser maior que 0")
        
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano, especial=False):
        if dano < 0:
            raise ValueError("O dano não pode ser negativo")
        
        # Lógica de defesa que reduz o dano
        if especial:
            dano = dano // 3  # Se for um ataque especial, reduz o dano para um terço
        else:
            dano = dano // 2  # Se for um ataque normal, reduz o dano pela metade
        
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    @abstractmethod
    def atacar(self, alvo):
        pass
    
    @abstractmethod
    def ataque_especial(self, alvo):
        pass

# Classe Heroi que herda de Personagem
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def atacar(self, alvo):
        dano = self.get_nivel() * 2
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
    def ataque_especial(self, alvo):
        dano = self.get_nivel() * 5  # Ataque especial causa mais dano
        alvo.receber_ataque(dano, especial=True)
        print(f"{self.get_nome()} usou um ataque especial em {alvo.get_nome()} e causou {dano} de dano!")

# Classe Inimigo que herda de Personagem
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
    
    def atacar(self, alvo):
        dano = self.get_nivel() * 1.5
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
    def ataque_especial(self, alvo):
        dano = self.get_nivel() * 4  # Ataque especial causa mais dano
        alvo.receber_ataque(dano, especial=True)
        print(f"{self.get_nome()} usou um ataque especial em {alvo.get_nome()} e causou {dano} de dano!")

# Classe Jogo
class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")
    
    def iniciar_batalha(self):
        print("Iniciando a batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            try:
                escolha = input("\nEscolha (1 - Ataque Normal, 2 - Ataque Especial): ")
                if escolha == '1':
                    self.heroi.atacar(self.inimigo)
                elif escolha == '2':
                    self.heroi.ataque_especial(self.inimigo)
                else:
                    print("Escolha inválida. Tente novamente.")
                    continue

                # Inimigo ataca de volta ou usa ataque especial
                if self.inimigo.get_vida() > 0:
                    escolha_inimigo = input("\nInimigo ataca! (1 - Ataque Normal, 2 - Ataque Especial): ")
                    if escolha_inimigo == '1':
                        self.inimigo.atacar(self.heroi)
                    elif escolha_inimigo == '2':
                        self.inimigo.ataque_especial(self.heroi)
                    else:
                        print("Escolha do inimigo inválida. Ataque normal por padrão.")
                        self.inimigo.atacar(self.heroi)

            except ValueError as ve:
                print(f"Erro: {ve}")
        
        if self.heroi.get_vida() > 0:
            print("\nVocê venceu!")
        else:
            print("\nVocê perdeu!")

# Iniciar o jogo
jogo = Jogo()
jogo.iniciar_batalha()
