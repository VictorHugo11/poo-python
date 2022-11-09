# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Gabriel Lacerda Abilio
# ALUNO 2: Gildasio Santos Xavier Filho
# ALUNO 3: Igor dos Santos Ferreira
# ALUNO 4: Victor Hugo Silva Nunes
# ALUNO 5: Guilherme Lima dos Santos
# ALUNO 6:


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.valor_fixo_material = 147.00
        self.valor_fixo_letra = 0.35

    def calcular_total(self):
        letras = len(self.frase.replace(" ", ""))
        area = self.altura * self.largura
        custoMaterial = area * self.valor_fixo_material
        custoDesenho = letras * self.valor_fixo_letra
        total = custoMaterial + custoDesenho
        return total


class Historico:
    def __init__(self):
        self.pedidos = []

    def inserir_pedido(self, pedido):
        self.pedidos.append(pedido.calcular_total())

    def calcular_faturamento(self):
        total = sum(self.pedidos)
        return total
