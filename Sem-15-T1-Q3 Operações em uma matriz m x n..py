matriz=[]
n=int(input('').strip())
m=int(input('').strip())
s=0
for l in range(n):
    lista=[]
    for c in range(m):
        e=int(input('').strip())
        lista.append(e)
        s+=e
    matriz.append(lista)     
#print(matriz)
somal=0
for c in range(m):
    somal+=matriz[0][c]

somac=0
for l in range(n):
    somac += matriz[l][m-1]
media=round((s/(n*m)),4)
q=maior=menor=0
for linha in matriz:
    for ele in linha:
        q+=1
        if q==1:
            maior=menor=ele
        else:
            if ele>maior:
                maior=ele
            if ele<menor:
                menor=ele
tupla=somal, somac, media, menor, maior
print(tupla)