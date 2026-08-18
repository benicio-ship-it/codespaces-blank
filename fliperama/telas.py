# ==============================================================
# ARQUIVO    : telas.py
# Disciplina : 2026-PCAP
# Aula       : 20
# Autor      : Benicio Cordeiro
# Data       : 04/08/2026
# Conceitos  : 
# ==============================================================

# Definição da Moldura Characteres e Tamanho
CAR = "#"
TAM = 40

# Desenha uma linha na tela
def linha():
    print(CAR * TAM)

# Desenha um texto de linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()