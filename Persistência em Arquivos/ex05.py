nota = open("notas.txt", "r", encoding="UTF-8")

for linha in nota:
    notas = []
    notas = linha.split()
    for i in range(4):
        notas[i] = float(notas[i])
    med = sum(notas) / len(notas)
    print(f'Média {med:.2f}')
