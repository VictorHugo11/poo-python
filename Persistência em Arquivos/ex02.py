arquivo = open("arquivo.txt", "r", encoding="UTF-8")
ls = []

for i in arquivo:
    i = i.strip('\n')
    i = int(i)
    ls.append(i)

print(sum(ls))
