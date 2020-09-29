def percentage_acrescism():
    price_old = float(input("Digite o preço antigo do produto: "))
    price_new = float(input("Digite o preço novo do produto: "))
    r = (100 * price_new - 100 * price_old) / price_old
    print("o percentual de acrescimo é de:",r,"%")
def main():
    
    percentage_acrescism()
    
main()    
