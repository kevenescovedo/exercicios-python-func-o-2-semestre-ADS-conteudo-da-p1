def multiply_two_numbers(number1,number2):
    result = number1 * number2
    return result
def main() :
    number_input1 = float(input("Digite o primeiro numero para multiplicar: "))
    number_input2 = float(input("Digite o segundo número para multiplicar: "))
    result_print = multiply_two_numbers(number_input1, number_input2)
    print(number_input1,"multiplicado por", number_input2 ,"é:",result_print)

main()    
    
