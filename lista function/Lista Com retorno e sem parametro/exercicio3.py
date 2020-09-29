def area():
    
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo "))
    area = (base * altura)/2
    return base,altura,area
def main() :
    
    result_print = area()
    print("o triangulo de base", result_print[0],"e de altura", result_print[1] ,"tem uma aréa de",result_print[2])
main()    
