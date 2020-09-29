def divisible():
    a = int(input("digite um numero para letra a: "))
    b = int(input("digite um numero para letra b: "))
    c = int(input("digite um numero para letra c: "))
    qtd = 0;
    if b % a == 0:
       qtd = qtd + 1
    if c % a == 0:
        
       qtd = qtd + 1
    if b % c == 0:
        
       qtd = qtd + 1
    if c % b == 0:
       qtd = qtd + 1
        
  
       
    print("quantidades  de números divisiveis por a:", qtd)  
def main():
    divisible()
main()    
    

       
         
        
            
                 
              
            
