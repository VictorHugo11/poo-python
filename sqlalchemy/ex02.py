
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///server.db")
connection = engine.connect()


session = Session()


Base = declarative_base(engine)


connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")



class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):   # Método construtor da classe
        self.nome = nome

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor):   # Método construtor da classe
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor


autor1 = Autor('Charles Duhigg')
autor2 = Autor('Sun Tzu')
lista = [autor1, autor2]
session.add_all(lista)
session.commit()

livro1 = Livro('O poder do hábito', 123, 1)
livro2 = Livro('A arte da guerra', 254, 2)
lista = [livro1, livro2]
session.add_all(lista)
session.commit()

print('-'*30)
result = session.query(Autor)           # retorna lista de objetos
for i in result:
    print(i.id, 'Autor:', i.nome)

print('-'*30)
result = session.query(Livro)           # retorna lista de objetos
for i in result:
    print(i.id,'Nome:', i.titulo, 'Paginas:', i.paginas, 'Autor:', i.autor)


