mes=['Janeiro:', 'Fevereiro:', 'Março:', 'Abril:', 'Maio:', 'Junho:', 'Julho:', 'Agosto:', 'Setembro:', 'Outubro:', 'Novembro:', 'Dezembro:']
lista=[]

for x in range(12):
    n=float(input('').strip())
    t=str(input('').upper().strip())
    if t =='C':
        n=n+273.15
        n=round(n,2)
        lista.append(n)
        
    elif t=='F':
        n=5*(n-32)/9+273.15
        n=round(n,2)
        lista.append(n)
        
    elif t=='K':
        lista.append(n)
        
    
#print(lista)
soma=sum(lista)
media=soma/12
media=round(media,2)
print('TEMPERATURA MÉDIA ANUAL')
print(f'{media}K')
print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
x=0
for i in lista:
    if i > media:
        print(f'{mes[x]} {i}K')
    x+=1
