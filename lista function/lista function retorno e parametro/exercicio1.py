def multiply_for_two(number):
    result = number * 2
    return result
def main() :
    number_input = float(input("Digite um número para que ele seja multiplicado por 2: "))
    result_print = multiply_for_two(number_input)
    print(number_input,"multiplicado por 2 é: ", result_print)

main()    
    
