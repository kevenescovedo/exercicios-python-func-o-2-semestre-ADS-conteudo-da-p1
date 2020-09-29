def multiply_for_two():
    number = float(input("Digite um número para que ele seja multiplicado por 2: "))
    result = number * 2
    return result,number
def main() :
   
    result_print = multiply_for_two()
    print(result_print[1],"multiplicado por 2 é: ", result_print[0])

main() 
