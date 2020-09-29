def calculadora(n1,n2,opera):
    if opera == '+':
        return n1 + n2
    elif opera == '-':
        return n1 - n2
    elif opera == '*':
        return n1 * n2
    elif opera == "/":
        return n1/n2
    else:
        return "operadores invalidos, por favor digite + para somar, - para tirar, * multiplicar e / para dividir"
def menu():
    print("--------------Calculadora---------------------------------------"
    print("+ para somar")
    print("- para subtrair")
    print(" * para multiplicar")
    print(" / para dividir")
        
def main():
    resposta = "s"
    while resposta == "s":
         menu()
         opera_input=input("por favor digite um sina de operação sendo eles os principais, + para somar, - para tirar, * multiplicar e / para dividir")
         n1_input= float(input("digite o primeiro numero para operação: "))
         n2_input= float(input("digite o segundo numero para operação: "))
         
         print("o resultado é:",calculadora(n1_input,n2_input,opera_input))
         resposta = input("digite s minusculo se você deseja continuar")
main()
         
               
         
         
    
    
    
    

    
    
    
    
