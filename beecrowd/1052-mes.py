'''
Problema: beecrowd | 1052
Data: 2026.05.07
Estudante: Benício Cordeiro
'''

# Objetivo: Identificar o valor que o usuário digita e atribuir um mes a ele

# --- ANÁLISE (LIAC) ---
# Entrada: A entrada contém um valor inteiro
# Processamento: non
# Saída: nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

y = int(input())

if y == 1:
    print('January')
elif y == 2:
    print("February")
elif y == 3:
    print("March")
elif y == 4:
    print("April")
elif y == 5:
    print("May")
elif y == 6:
    print("June")
elif y == 7:
    print("July")
elif y == 8:
    print("August")
elif y == 9:
    print("September")
elif y == 10:
    print("October")
elif y == 11:
    print("November")
elif y == 12:
    print("December")