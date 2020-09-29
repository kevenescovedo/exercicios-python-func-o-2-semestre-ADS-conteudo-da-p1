def matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input('Digite o valor de ['+ str(lin) + ','+ str(col) + ']: ')))
        matriz.append(linha)
    return matriz

def main():
    n_linhas = int(input('Digite o número linhas a ser inserida -> '))
    n_col = int(input('Digite o número colunas a ser inserida -> '))
    print(matriz(n_linhas, n_col))

main()
