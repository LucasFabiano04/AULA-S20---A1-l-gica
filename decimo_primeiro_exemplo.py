"""
TABUADA
"""

while True:
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))
    if numero == 0:
        break
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")