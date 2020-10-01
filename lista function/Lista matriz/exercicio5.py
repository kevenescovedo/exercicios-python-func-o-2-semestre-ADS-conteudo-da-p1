ef somar_diagonal():
    soma_acima = 0
    soma = 0
    matriz = []
    # for c in range(linha):
    for c in range(4):
        linhas = []
        for i in range(4):
        # for i in range(coluna):
            elementos = int(input('Digite o {}º elemento da {}ª linha: '.format(i + 1, c + 1)))
            if c == i:
                soma += elementos
            linhas.append(elementos)
        matriz.append(linhas)

    print('\n**Matriz gerada**')
    # for l in range (linha):
    for l in range (4):
        # for c in range (coluna):
        for c in range (4):
            if c > l:
                soma_acima += matriz[l][c]
            print(matriz[l][c] , end='   ')
        print()
    return print('A soma da diagonal principal é: {}\nA soma a soma dos números acima da diagonal é: {}'.format(soma, soma_acima))

def main():
    # m = int(input('Digite o número de linhas que quer inserir na matriz -> '))
    # n = int(input('Agora digite o número de colunas -> '))
    # somar_diagonal(m, n)
    somar_diagonal()

main()
