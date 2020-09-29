def percentage_salary(percentage, salary):
    percentage_of_part_salary = (percentage/100) * salary
    total_salary = salary + percentage_of_part_salary
    return  total_salary
def main() :
    salary_input = float(input("Digite o valor do salálario de um funcionario: "))
    percentage_input = float(input("Digite o valor da porcentagem de aumento do salário do funcionário: "))
    result_salary = percentage_salary(percentage_input, salary_input)
    print(percentage_input,"%,de salaário de", salary_input ,"é:",result_salary)

main()  
