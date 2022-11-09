class Filme:
    def __init__ (self, titulo, genero,):
        self.__titulo = titulo
        self.__genero = genero 

    def get_titulo(self):
        return self.__titulo
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, titulo):
        self.__titulo =  titulo
    def set_genero(self, genero):
        self.__genero = genero

listaFilmes = [] 

for i in range (3):
    nomeFilme = input('Digite o nome do filme: ')
    genero = input('Digite o genero: ')
    f = (Filme(nomeFilme, genero))
    listaFilmes.append(f)

for i in listaFilmes:
    print('=' * 15)
    print(f'Titulo: {i.get_titulo()}')
    print(f'Genero: {i.get_genero()}')