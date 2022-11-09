vg = ['a', 'e', 'i', 'o', 'u', ]
qtde_vg = 0

arq = open("palavra.txt", "r", encoding="UTF-8")

for letra in arq:
    print(letra)
    for i in letra:
        if i in vg:
            print(vg)
            qtde_vg += 1
print(qtde_vg)
