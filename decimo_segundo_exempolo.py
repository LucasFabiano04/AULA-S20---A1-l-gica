"""
CONTAGEM REGRESSIVA
"""
while True:
    numero = int(input("Digite um número para iniciar a contagem regressiva: "))
    
    while numero >= 0:
        print(numero)
        numero -= 1
    
    continuar = input("Quer fazer outra contagem regressiva? (s/n): ")
    if continuar.lower() == 'n':
        break