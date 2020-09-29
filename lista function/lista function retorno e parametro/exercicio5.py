
def media(p1,p2):
    media_result = (p1 + p2)/2
    return media_result
def aprovado(media):
    if media >= 6:
       return 'aprovado'
    elif media < 6:
        return 'reprovado'
    else:
        return "media imposivel , como assim ?"
def main():
    p1 = float(input("digite a nota da p1: "))
    p2 = float(input("digite a nota do p2: "))
    media_var =  media(p1,p2)
    print("media",media_var,aprovado(media_var))

main()   

 
    
    
        
