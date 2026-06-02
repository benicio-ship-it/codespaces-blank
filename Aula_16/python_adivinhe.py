# ==============================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : adivinha.py
# Autor      : Benício Cordeiro
# Data       : 2026.06.01
# ==============================================================================

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False
    
    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + "): "))
        
        if palpite == numero_secreto:
            print("Acertou!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
            
        chances = chances - 1
        print("Chances restantes:", chances)
        
    # Mudança aqui: retornamos o resultado E o número secreto
    return acertou, numero_secreto

# --- Níveis guardados em uma lista de listas: [nome, maximo, chances] ---
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 50, 5],
    ["Difícil", 100, 7],
    ["Impossivel", 1000, 10],
]

# --- Menu de escolha do nível ---
print("Escolha a dificuldade:")
print("1 - Fácil       (1 a 10, 3 chances)")
print("2 - Médio       (1 a 50, 5 chances)")
print("3 - Difícil     (1 a 100, 7 chances)")
print("4 - Impossível  (1 a 1000, 10 chances)")
opcao = int(input("Digite 1, 2, 3 ou 4:"))

# A opção 1 está na posição 0 da lista, por isso o ajuste
nivel = niveis[opcao - 1]

# --- Iniciamos o jogo com a configuração do nível escolhido ---
print("Você escolheu o nível:", nivel[0])

# Mudança aqui: recebemos as duas respostas
venceu, numero_resposta = jogar(nivel[1], nivel[2])

if not venceu:
    print("Game Over!")
    # Agora a variável existe no código principal e pode ser mostrada
    print(f"O número correto era o: {numero_resposta}")