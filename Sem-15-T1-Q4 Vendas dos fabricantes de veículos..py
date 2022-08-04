fabricante='Fiat', 'Ford', 'GM', 'Wolkswagen'
ano=[2013, 2014, 2015, 2016, 2017, 2018]
matriz=[]
for linha in range(4):
    linha=[]
    for coluna in range(6):
        n=int(input('').strip())
        linha.append(n)
    matriz.append(linha)
#print(matriz)
a=int(input('').strip())
a=ano.index(a)
q=maior=a1=0
for l in range(4):
    q+=1
    if q==1:
        maior=matriz[l][a]
        a1=l
    elif matriz[l][a]>maior:
        maior=matriz[l][a]
        a1=l
mai=[]
v=0
for l1 in range(6):
    soma=0
    for c1 in range(4):
        soma+=matriz[c1][v]
    v+=1
    mai.append(soma)
x=max(mai)    
x1=mai.index(x)
print(f'A fabricante que mais vendeu em {ano[a]} foi a {fabricante[a1]} com {maior} mil unidades.')
print(f'O ano de maior volume geral de vendas foi {ano[x1]} com {x} mil unidades.')
print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
media=[]
for l2 in range(4):
    soma_=0
    for c2 in range(6):
        soma_+=matriz[l2][c2]
    med=float(soma_/6)
    med=round(med,2)
    media.append(med)
    print(f'A {fabricante[l2]} vendeu em média {media[l2]} unidades por ano.')
