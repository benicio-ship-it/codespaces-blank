# ==============================================================
# ARQUIVO    : main.py
# Disciplina : 2026-PCAP
# Aula       : 20
# Autor      : Benicio Cordeiro
# Data       : 04/08/2026
# Conceitos  : 
# ==============================================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar

NOME_DO_DONO = "NORMAL🕹️"
NOME_DOS_JOGOS = ["Adivinhe o Numero", "Pedra-Papel-Tesoura"]
OPCOES = ["0", "1", "2"]
vezes_jogado = carregar_placar()

print(carregar_placar())

def mostrar_placar():
    titulo("PLACAR")
    for i in range(3):
        print(NOME_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "x")

while True:
    titulo('🕹️  FLIPERAMA ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('2 - Jogo Pedra, Papel e Tesoura')
    print('0 - Sair')
    linha()
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        titulo("Tchau...")
        break
    elif opcao == '1':
        jogar_adivinhe()

    elif opcao == '2':
        jogar_ppt()
    else:
        print('Opção inválida! Tente novamente.')

indice = int(opcao) - 1
vezes_jogado[indice] = vezes_jogado[indice] + 1