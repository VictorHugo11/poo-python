arquivo = open("arquivo.txt", "w", encoding="UTF-8")

for i in range(10):
    num = input('digite 10 numeros: ')
    arquivo.write(num + '\n')
