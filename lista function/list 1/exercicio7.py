def media():
    n1 = float(input("digite a primeira nota: "))
    n2 = float(input("digite a segunda nota: "))
    n3 = float(input("digite a primeira nota: "))
    letra = input("dgite a para média aritmetica e a p para média ponderada: ")
    if letra == "A" or letra == "a":
        media = (n1 + n2 + n3)/3
        print("media do aluno: ", media)
    elif letra == "P" or letra == "p":
      media = (5*n1 + 3*n2 + 2*n3)/(5 + 2 + 3)
      print("media do aluno: ", media)
    else:
        print("por favor digite uma letra valida ou seja P ou A")
def main():
    media()
main()    
        
         
    
