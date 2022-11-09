class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print(self.nome)
        print(self.idade)
        print(self.ra)


class Aluno(Pessoa):
    def __init__(self, nome, idade, ra):
        super().__init__(nome, idade)
        self.ra = ra

    # def exibir(self):
    #     super().exibir()
    #     print(self.ra)


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


aluno1 = Aluno('Paulo', 22, 2001610)
aluno1.exibir()
