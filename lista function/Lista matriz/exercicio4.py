def matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input('1 matriz Digite o valor de ['+ str(lin) + ','+ str(col) + ']: ')))
        matriz.append(linha)
    return matriz

def matriz2(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input('2 matriz Digite o valor de ['+ str(lin) + ','+ str(col) + ']: ')))
        matriz.append(linha)
    return matriz
def mm(a_mat, b_mat):
    multiplica = []
    result_mat = 0
    if len(a_mat[0]) == len(b_mat):
        for x in range(len(a_mat[0])):
            result_mat = 0
            for y in range(len(b_mat[x])):
                result_mat = a_mat[x][y] * b_mat[y][x] + result_mat
                
            multiplica.append(result_mat)
            

        return multiplica       
                       
                       
                       
        
def main():
    n_linhas = int(input('Digite o número linhas a ser inserida na 1 matriz -> '))
    n_col = int(input('Digite o número colunas a ser inserida na 1 matriz -> '))
    n_linhas2 = int(input('Digite o número linhas a ser inserida na 2 matriz -> '))
    n_col2 = int(input('Digite o número colunas a ser inserida na 2 matriz -> '))
    a_mat = matriz(n_linhas, n_col)
    b_mat = matriz2(n_linhas2, n_col2)
    
    print(mm(a_mat,b_mat))
    
    

main()

    
