"""
CONTAR VOGAIS
"""
while True:
    palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
    if palavra == "":
        break

    vogais = "aeiouAEIOU"
    contagem_vogais = sum(1 for letra in palavra if letra in vogais)
    
    print(f"A palavra '{palavra}' tem {contagem_vogais} vogais.")