# Conserto 1: trecho do "Adivinhe o Numero" (Aula 16)
import random

print(" === ADIVINHE O NUMERO === ")
segredo = random.randint(1, 10)
palpite = int(input("Digite um numero de 1 a 10: "))
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)