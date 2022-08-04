def soma_todo_faturamento_filial(matriz, filiais):
    i_filial = -1
    i_ano = -1
    valor_periodo_filial = []
    for filial in filiais:
        i_filial += 1
        soma = 0
        for ano in matriz:
            soma += ano[i_filial]
        valor_periodo_filial.append(soma)

    return valor_periodo_filial

def faturamento_por_ano(matriz_tri):
    matriz_linha_faturamento_ano = []
    for ano in matriz_tri:
        matriz_linha_faturamento_ano.append(sum(ano))
    return matriz_linha_faturamento_ano

def faturamento_ano_filial(matriz_tri):
    matriz_tridimensional = []
    for  ano in matriz_tri:
        matriz_linha_coluna_faturamento_ano = []
        for filial in ano:           
            faturamento_filial_ano = 0
            for mes in filial:
                faturamento_filial_ano += mes[3]
            matriz_linha_coluna_faturamento_ano.append(faturamento_filial_ano)            
        matriz_tridimensional.append(matriz_linha_coluna_faturamento_ano)    
    return matriz_tridimensional

def preenche_matriz( matrizes_bi, linhas , elementos):
    matriz_tridimencional = [] 
    for ano in matrizes_bi:
        matriz_bidimencional = [] 
        for filial in linhas:
            linha = []         
            for mes in elementos:
                
                faturamento_mes = int(input(f''))
                
                linha.append((ano, filial, mes, faturamento_mes))
            
            matriz_bidimencional.append(linha)
        
        matriz_tridimencional.append(matriz_bidimencional)
    return matriz_tridimencional

def main():
    
    filiais = ('Filial 1', 'Filial 2', 'Filial 3')
    lista_meses = ( 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    periodo = list(ano for ano in range(2014, 2018))

    
    faturamento_anual = preenche_matriz(periodo, filiais, lista_meses)
    faturamento_por_ano_filial = faturamento_ano_filial(faturamento_anual)
    faturamento_total_por_ano = faturamento_por_ano(faturamento_por_ano_filial)
    faturamento_total_do_periodo_por_filial = soma_todo_faturamento_filial(faturamento_por_ano_filial, filiais)

       
    i_ano = -1
    for ano in faturamento_anual:
        i_ano += 1
        i_filial = -1
        for filial in ano:
            i_filial += 1
            i_mes = -1
            for mes in filial:
                i_mes += 1
                print(f'{filial[i_mes][0]};{filial[i_mes][1]};{filial[i_mes][2]};{filial[i_mes][3]}')
            
            print(f'TOTAL {filial[i_mes][0]} {filial[i_mes][1].upper()};{faturamento_por_ano_filial[i_ano][i_filial]}' )
        print(f'TOTAL {filial[i_mes][0]} TODAS FILIAIS;{faturamento_total_por_ano[i_ano]}')
    print(f'TOTAL PERÍODO TODAS FILIAIS;{sum(faturamento_total_do_periodo_por_filial)}')
        
if __name__ == '__main__':
    main()