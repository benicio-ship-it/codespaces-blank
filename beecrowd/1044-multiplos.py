'''
Problema: beecrowd 1044
Data: 2026.04.16
Estudante: Benício Cordeiro
'''
#Objetivo: Verificar se dois inteiros são múltiplos entre si

# ___ ANÁLISE (LIAC) ___
#Entrada: dois inteiros A e B na mesma linha separados por espaço
#Processo: identificar maior e menor. verificar se maior % menor == 0
#Saída: "São multiplos" ou "Não são Multiplos"

A,B = input().split()
A = int(A)
B = int(B)

# Identifica maior e menor para aplicar o operador % corretamente
# (o resto sempre deve ser calculado dividindo o maior pelo menor)
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

# Operador % (módulo): retorna o resto da divisão inteira
# Se o resto for 0, o maior é multiplo do menor são multiplos entre si
if maior % menor == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")