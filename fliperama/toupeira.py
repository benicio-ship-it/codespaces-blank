# ===================================================================
# ARQUIVO   : toupeira.py (pasta fliperama)
# Conceitos : Loop acelerado, exibição vertical aleatória, tempo limite, antispam
# Autor     : Benício Cordeiro
# Data      : 2026.09.01
# ===================================================================

import sys
from random import randint
from time import sleep, time
from telas import titulo, linha


def tecla_pressionada():
    if sys.platform == 'win32':
        import msvcrt
        return msvcrt.kbhit()
    else:
        import select
        prontos, _, _ = select.select([sys.stdin], [], [], 0)
        return len(prontos) > 0


def limpar_teclado():
    if sys.platform == 'win32':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import select
        while select.select([sys.stdin], [], [], 0)[0]:
            sys.stdin.readline()


def jogar_toupeira():
    titulo('JOGO CAÇA A TOUPEIRA')
    print('Pegue as 5 toupeiras para ganhar!')
    input('Pressione ENTER para começar...')
    
    limpar_teclado()
    pontos = 0
    
    while pontos < 5:
        quantidade_buracos = randint(2, 5)
        
        for _ in range(quantidade_buracos):
            print('🕳️')
            
            if tecla_pressionada():
                limpar_teclado()
                print('Perdeu! Você clicou na hora errada!')
                linha()
                return
                
            sleep(randint(2, 5) / 10)
        
        # A toupeira aparece na tela
        print('🐹')
        
        tempo_inicial = time()
        input()
        tempo_final = time()
        
        tempo_reacao = tempo_final - tempo_inicial
        
        if tempo_reacao <= 0.5:
            pontos += 1
            print(f'💥-🔨 {pontos}/5')
        else:
            print('Perdeu, Você Demorou Demais')
            linha()
            return
            
        sleep(0.3)

    print('Você pegou todas as toupeiras!')
    linha()