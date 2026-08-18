# ==============================================================
# ARQUIVO    : ppt.py
# Disciplina : 2026-PCAP
# Aula       : 20
# Autor      : Benicio Cordeiro
# Data       : 11/08/2026
# Conceitos  : Jogo com modulo, lista como tabela de nomes, função com retorno,
#                 operador % para dar a volta
# ==============================================================

# importa função randint da biblioteca random, que sorteia um número inteiro
# aleatóiro em um intervalo definido
from random import randint

# importa as funções título e linha do arquivo telas.py
from telas import titulo, linha

# importa a função ler_opcao que validaa entrada do usuário do arquivo modulos.py
from modulos import ler_opcao

# lista com PEDRA == posição 0 ; PEPEL == 1 ; TESOURA == 2
JOGADAS = ["PEDRA", "PAPEL", "TESOURA"]

# define o ganhador
def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    elif jogador == (computador + 1) % 3:
        return "jogador"
    return "computador"

# mostra as opções de jogada
def mostrar_jogadas():
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")
    linha()

def jogar_ppt():
    titulo("PEDRA - PAPEL - TESOURA")

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao("Sua Jogada", ["0", "1", "2"]))
        computador = randint(0, 2)

        print("Você jogou " + JOGADAS[jogador] + ".")
        print("O computador jogou " + JOGADAS[computador] + ".")

        resultado = quem_vence(jogador, computador)

        if resultado == "empate":
            print ("Empate, ninguém ganhou!")
        elif resultado == "jogador":
            pontos_jogador += 1
            print("Você venceu essa rodada")
        elif resultado == "computador":
            pontos_computador += 1
            print("Computador venceu essa rodada!")

        linha()
        print(f"Placar: Jogador {pontos_jogador}  X  {pontos_computador}  Computador")
        linha()

    if pontos_jogador > pontos_computador:
        titulo("Você ganhou!")
    else:
        titulo("Você perdeu!")