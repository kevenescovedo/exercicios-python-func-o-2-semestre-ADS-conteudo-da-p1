def area():
    
    lado = float(input("Digite o quanto mede o lado dos quadrados: "))
    
    area = lado * lado
    return lado,area
def main() :
    
    result_print = area()
    print("o quadrado que possui lados iguais a", result_print[0],"tem uma aréa de",result_print[1])
main()    

