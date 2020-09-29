def percentage_salary(percentage, salary):
    percentage_of_part_salary = (percentage/100) * salary
    total_salary = salary + percentage_of_part_salary
    return  total_salary
def main() :
    total_old_salary = 0;
    total_new_salary = 0;
    for x in range(10):
     salary_input = float(input("Digite o valor do salálario de um funcionario: "))
     total_old_salary = salary_input + total_old_salary
     percentage_input = float(input("Digite o valor da porcentagem de aumento do salário do funcionário: "))
     
     result_salary = percentage_salary(percentage_input, salary_input)
     total_new_salary = result_salary + total_new_salary
     print(percentage_input,"%,de salaário de", salary_input ,"é:",result_salary)
     
    dif_total = total_new_salary - total_old_salary
    print("a diferença entre os salários antigos que eram de",total_old_salary,"e os novos que são de",total_new_salary,"é de:",dif_total)
main()  
