"""
CLASSE é como se fosse as possiveis entradas de dados do programa e dentro das classes os ATRIBUTOS são as variaveis
CLASSE é como se fosse uma foroma para a entrada de dados
Toda vez que eu tiver uma entrada de dadoas no formato da minha CLASSE eu terei um novo OBJETO
Desta forma eu terei um OBJETO no formato da minha CLASSE, ou seja, INSTANCIAS da minha CLASSE 
MÉTODOS são as ações que podem ser realizadas com essas entradas
"""

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    
    def get_numero(self):
        return self.__numero

    
    def set_numero(self, numero):
        self.__numero = numero
        return self.__numero

    
    def get_titular(self):
        return self.__titular

    
    def set_titular(self, titular):
        self.__titular = titular
        return self.__titular

    
    def get_saldo(self):
        return self.__saldo

    
    def set_saldo(self, saldo):
        self.__saldo = saldo
        return self.__saldo
    
    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
        return self.__limite

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print(f'Numero da conta: {self.__numero}\nSaldo: {self.__saldo}')