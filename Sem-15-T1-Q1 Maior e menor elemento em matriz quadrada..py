matriz=[]
num=int(input('').strip())
for linha in range(num):
    linha=[]
    for coluna in range(num):
        n=int(input('').strip())
        linha.append(n)
    matriz.append(linha)
#print(matriz)

maior=menor=quant=0
l1=c1=l2=c2=0
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        quant+=1
        if quant == 1:
            maior=menor=matriz[l][c]
            l1=l=l2
            c1=c=c2
        else:
            if matriz[l][c] > maior:
                maior=matriz[l][c]
                l1=l
                c1=c
            if matriz[l][c] < menor:
                menor=matriz[l][c]
                l2=l
                c2=c
print(f'({l1}, {c1})')
print(f'({l2}, {c2})')