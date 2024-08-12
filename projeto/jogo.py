# Personagem: Classe Mãe
# Heroi: Controlado pelo usuario
# Inimigo: Adversario do usuario


class Personagem:
    def __init__(self,nome,vida,nivel) -> None:
        self._nome = nome
        self._vida = vida
        self._nivel = nivel
    
    def get_nome(self):
        return self._nome
    
    def get_vida(self):
        return self._vida
    
    def get_nivel(self):
        return self._nivel
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel) -> None:
        super().__init__(nome, vida, nivel)