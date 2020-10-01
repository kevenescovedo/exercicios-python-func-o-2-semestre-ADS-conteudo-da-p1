def adicionar_itens():
  lojas=[]
  produtos=[]
  preco_p = []
  matriz = []
  for l in range(4):
    lojas.append(input("digite nome da loja: "))
  for c in range(2):
    produtos.append(input("digite nome dos produtos: "))
  for l in range(4):
    preco_p = []
    for c in range(2):
      preco_p.append(float(input("digite o valor do produto:" )))
    matriz.append(preco_p)
  for l in range(4):
    for c in range(2):
      if matriz[l][c] <= 120:
        print("O {} da loja {} tem o preco abaixo de 120,00 reais ".format(produtos[c], lojas[l]))

def main():
  adicionar_itens()

main()
