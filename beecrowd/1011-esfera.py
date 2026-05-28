'''
Problema:beecrowd 1011
2026.04.09
Benício Cordeiro
'''

#Objetivo: Ler o raio de uma esfera e calcular seu volume com a fórmula (4/3) * pi R³

# ---ANÁLISE (LIAC)---
#Entrada: um número de ponto flutuante (o raio R)
#Saída: exibir no formato "VOLUME = valor" com 3 casas decimais 

#float() Converte o valor lido para número decilam (ponto flutuante)
R = float (input())

#O enunciado pede para atribuir pi como constante - não usar math.pi
pi = 3.14159

#3.0/3 garante divisão decimal (não inteira) - conforme dica do enunciado
#R** R elevado á terceira potência (R³)
V = (4.0 / 3 ) * pi * R ** 3

# :.3f Formata o númeor com exatamente 3 casas decimais
print(f"VOLUME = {V:.3f}")