def inicio_fim_jogo():
    hora_inicial = int(input("Digite a hora inicial do jogo: "))
    min_inicial = int(input("Digite o minuto em que o  jogo inicia: "))
    hora_final = int(input("Digite a hora em que o jogo termina: "))
    min_final = int(input("Digite o minuto em que o  jogo termina: "))
    if(min_inicial > min_final):
       min_final = min_final + 60
       hora_final = hora_final - 1
    if(hora_inicial > hora_final):
       hora_final = hora_final + 24
minuto_duracao = min_final - min_inicial
hora_duracao = hora_final - hora_inicial
print("o jogo dura:", hora_duracao,"horas e",minuto_duracao,"minutos")
def main():
    inicio_fim_jogo()
main()   
    
