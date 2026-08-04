# ==============================================================
# ARQUIVO    : modulos.py
# Disciplina : 2026-PCAP
# Aula       : 20
# Autor      : Benicio Cordeiro
# Data       : 04/08/2026
# Conceitos  : Depois do que
# ==============================================================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas:
        print('opcao invalida, tente novamente')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))