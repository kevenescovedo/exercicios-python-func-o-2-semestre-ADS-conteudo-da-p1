def seq():
    termos = int(input('Digite um número '))
    e = 1
    for fat in range(1,termos+1):
      fatorial = 1  
      i=1
      while i <= fat:
        fatorial = fatorial * i 
        i = i + 1
      print('O fatorial de {} é {}.'.format(fat,fatorial))
      e = e + (1 / fatorial)
      print('E=',e)
def main():
    seq()
main()    
    
