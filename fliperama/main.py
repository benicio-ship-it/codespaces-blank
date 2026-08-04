# ==============================================================
# ARQUIVO    : main.py
# Disciplina : 2026-PCAP
# Aula       : 20
# Autor      : Benicio Cordeiro
# Data       : 04/08/2026
# Conceitos  : Depois do que
# ==============================================================

# importar funções de arquivos (módilos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe

NOME_DO_DONO = "NORMAL 🕹️"

while True:
    titulo('🕹️ FLIPERAMA ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('0 - Sair do Fliperama')
    linha()
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '0':
        print("Até a próxima! Suíno...")
        break

    elif opcao == '1':
        jogar_adivinhe()
    else:
        print('Opção inválida! Tente novamente.')