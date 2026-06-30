# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Benício Cordeiro
# Data       : 30/06/2026
# ════════════════════════════════════════════════════════════

import random

# Verifica quem venceu a rodada.
def quem_venceu(soma, aposta):
    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if resultado == aposta:
        return "Jogador"
    else:
        return "Máquina"


def jogar():

    maquina = random.randint(0, 5)

    while True:
        jogador = int(input("Escolha um número (0-5): "))
        if 0 <= jogador <= 5:
            break
        print("Número inválido!")

    while True:
        aposta = input("Par ou Ímpar? ").lower()

        if aposta == "ímpar":
            aposta = "impar"

        if aposta == "par" or aposta == "impar":
            break

        print("Digite apenas 'par' ou 'ímpar'.")

    soma = jogador + maquina
    vencedor = quem_venceu(soma, aposta)

    print("   RESULTADOS:")

    if soma % 2 == 0:
        print("Resultado: PAR")
    else:
        print("Resultado: ÍMPAR")

    print("Vencedor:", vencedor, "\n")

    return vencedor


def main():

    jogador = 0
    maquina = 0

    print("PAR OU ÍMPAR")

    while jogador < 3 and maquina < 3:

        vencedor = jogar()

        if vencedor == "Jogador":
            jogador =+ 1
        else:
            maquina =+ 1

        print("Placar:", jogador, "x", maquina, "\n")

    print("Acabou!")

    if jogador == 3:
        print("Jogador Venceu!")
    else:
        print("Máquina Venceu!")

# Inicia o programa.
main()