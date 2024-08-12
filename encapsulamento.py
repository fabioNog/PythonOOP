print("\n Exemplo de Encapsulamento")

class ContaBancaria:
    def __init__(self,saldo) -> None:
        self.__saldo = saldo # o __ faz com este atributo seja privado
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da Conta: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da Conta: {conta.consultar_saldo()}")

conta.sacar(valor=500)
print(f"Saldo da Conta: {conta.consultar_saldo()}")
