def number_perfect():
    array = []
    number = int(input("digite um número: "))
    for x in range(number):
        if x > 0:
          if number % x == 0:
             array.append(x)
          if len(array) == 3:
             return array
def main():
    print(number_perfect())
main()    
            
        
    
