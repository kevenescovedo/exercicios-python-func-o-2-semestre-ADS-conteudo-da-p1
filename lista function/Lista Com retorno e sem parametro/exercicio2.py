def sub_two_numbers():
    
    number1 = float(input("Digite o primeiro numero para subtrair: "))
    number2 = float(input("Digite o segundo número para subtrair: "))
    result = number1 - number2
    return number1,number2,result
def main() :
    
    result_print = sub_two_numbers()
    print(result_print[0],"subtraido por", result_print[1] ,"é:",result_print[2])
main()    
