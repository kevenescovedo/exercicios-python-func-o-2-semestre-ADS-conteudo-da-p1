def simetria(a,b): 
    if len(a[0]) == len(b):
        c = []
        for l in range (len(a)): 
            c.append([]) 
            for xxx in range (len(b[0])):
                c[l].append(0)
                for m in range (len(a[0])):
                    c[l][xxx] += a[l][m] * b[m][xxx]
        return c
    else:
        return False

def main():
    num_linhas = int(input('Digite o Número de Linhas : '))
    num_colunas = int(input('Digite o Número de Colunas: '))
    a = []
    for lin in range(num_linhas): 
        linha = []
        for col in range(num_colunas):
            linha.append(int(input('Digite o valor de [' + str(lin) + ',' + str(col) + ']: ')))
        a.append(linha)
    num_linhas = int(input('Digite o Número de Linhas : '))
    num_colunas = int(input('Digite o Número de Colunas: '))
    b = []
    for lin in range(num_linhas): 
        linha = []
        for col in range(num_colunas):
            linha.append(int(input('Digite o valor de [' + str(lin) + ',' + str(col) + ']: ')))
        b.append(linha)
    
    print(simetria(a,b))  

main()

    
