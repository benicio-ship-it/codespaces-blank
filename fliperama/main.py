# =======================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Benício Cordeiro
# Data:         2026.08.04
# Conceitos:    Menu principal, gerenciamento de estado e fluxo do app
# =======================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from toupeira import jogar_toupeira
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
NOME_DO_DONO = 'BENICIO'
NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Caça a Toupeira']

vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()


def mostrar_placar():
    titulo('PLACAR')
    for i in range(len(NOMES_DOS_JOGOS)):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
    linha()


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('5 - Jogadores')
    print('4 - Caça a Toupeira')
    print('3 - Par ou Ímpar')
    print('2 - Pedra - Papel - Tesoura')
    print('1 - Jogo Adivinhe o Número')
    print('0 - Sair do Fliperama')
    linha()

    opcao = ler_opcao('Escolha uma opção', ['0', '1', '2', '3', '4', '5'])

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo('Ate a proxima!')
        break

    if opcao == '5':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] += 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()
        elif opcao == '4':
            jogar_toupeira()

        input('Pressione Enter para voltar ao menu... ')