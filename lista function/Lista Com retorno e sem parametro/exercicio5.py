def leitura_valor():
  numero = int(input("digite um numero para saber se ele é par ou impar: "))
  if numero % 2 == 0:
   
    return "É par"
  else:
     return 'É impar'
def main():
  print(leitura_valor())
main()  
