from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        self.salario_base += (self.salario_base * 0.1)
        return self.salario_base


gerente1 = Gerente('Gil', 111111, 10000)
assistente1 = Assistente('Gabriel', 222222, 5000)
vendedor1 = Vendedor('Igor', 333333, 2500)

lista = []

lista.append(gerente1)
lista.append(assistente1)
lista.append(vendedor1)

for i in lista:
    print('Nome:', i.nome)
    print('Salario:', i.calcular_salario())
