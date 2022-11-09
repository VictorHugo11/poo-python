
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///server.db")
connection = engine.connect()


session = Session()


Base = declarative_base(engine)


connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INT,
                        SALARIO FLOAT)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):   # Método construtor da classe
        self.nome = nome
        self.idade = idade
        self.salario = salario


func1 = Funcionario('Gil', 19, 4500)
func2 = Funcionario('Victor', 23, 6500)
func3 = Funcionario('Guilherme', 29, 2500)
func4 = Funcionario('Gabriel', 20, 4500)

lista = [func1, func2, func3, func4]
session.add_all(lista)
session.commit()

print('-'*30)
result = session.query(Funcionario)           # retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.idade, i.salario)

print('-'*30)
d = session.query(Funcionario).filter(
    Funcionario.salario > 1500).order_by(Funcionario.nome)
for i in d:
    print(i.id, i.nome, i.idade, i.salario)


connection.close()
