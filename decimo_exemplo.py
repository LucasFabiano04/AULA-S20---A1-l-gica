"""
CALCULANDO A MÉDIA DAS NOTAS
"""

soma = 0
contagem = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): "))
    if nota == -1:
        break
    soma += nota
    contagem += 1

if contagem > 0:
    media = soma / contagem
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")