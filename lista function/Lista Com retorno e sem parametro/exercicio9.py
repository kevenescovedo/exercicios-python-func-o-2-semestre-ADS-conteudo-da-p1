def dados():
    idade = []
    sexo = [] 
    olhos = []
    cabelo = []
    media_idade = 0
    soma = 0
    maior_idade = -1
    mulheres = 0
    for n in range (2):
        idade.append(int(input('Informe a sua idade: ')))
        sexo.append(str(input('Informe seu sexo "A" = MASCULINO ou "B" = FEMININO: ')))
        olhos.append(str(input('Informe a cor dos olhos "A" = AZUIS ou "C" = CASTANHOS: ')))
        cabelo.append(str(input('Informe a cor do cabelo "L" = LOIRO , "P" = PRETO ou "C" = CASTANHO: ')))
        if (olhos[n] == "C" or olhos[n] == "c") and (cabelo[n] == "P" or cabelo[n] == "p"):
            media_idade = media_idade + idade[n]
            soma = soma + 1
        if idade[n] > maior_idade:
            maior_idade = idade[n]
        if ((sexo[n] == 'B' or sexo[n] == 'b') and (idade[n] >= 18 and idade[n] <= 35) and
            (olhos[n] == 'A' or olhos[n] == 'a') and (cabelo[n] == 'L' or cabelo[n] == 'l')):
            mulheres = mulheres + 1
    if soma != 0:
        media_idade = media_idade / soma
           
    return print('A média de idade das pessoas com olhos castanhos e cabelos pretos foi de : ', media_idade, 
    '\nA maior idade entre os habitantes é ', maior_idade, 'anos.'
    '\nMulheres com idade entre 18 e 38 anos, que tenham olhos azuis e cabelos louros: ', mulheres)

def main():
    dados()
    
main()
