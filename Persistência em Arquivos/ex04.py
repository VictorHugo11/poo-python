impares = open("num_impares.txt", "r", encoding="UTF-8")
pares = open("num_pares.txt", "r", encoding="UTF-8")

num = []

for i in impares:
    i = int(i)
    num.append(i)

for i in pares:
    i = int(i)
    num.append(i)

num.sort()

for i in num:
    print(i)
