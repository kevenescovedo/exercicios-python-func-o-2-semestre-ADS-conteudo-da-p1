def hours_and_seconds_minutes(segundos):
    
    h = segundos / 3600
    r = segundos % 3600
    m = r / 60
    s = r % 60
    print(f'{h:.00f}:{m:.00f}:{s:.00f}')
def main():
    segundos = int(input("Digite a quantidade de segundos para saber a hora e minuitos: "))
    hours_and_seconds_minutes(segundos)
main()     
    
    
    
