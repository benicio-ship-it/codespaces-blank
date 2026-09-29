'''
Problema: BeeCrowd 1007
Data: 2026.04.16
estudante: Benício Cordeiro
'''
#objetivo: ler quatro inteiros e calcular DIFERENCA = (A * B) - (C * D)

#--- ANÁLISE (LIAC) ---
#Entrada: quatro valores inteiros A, B, C e D (um por linha)
#processamento: diferença entre o produto A*B e o produto C*D
#saída: "DIFERENCA = valor" (inteiro, letras maíusculas, espaços ao redor do =)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Calcula a diferença dos produtos conforme a fórmula do enunciado
dif = (A * B) - (C * D)

print(f"DIFERENCA = {dif}")