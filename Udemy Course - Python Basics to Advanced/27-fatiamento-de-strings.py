"""
Fatiamento de strings
012345678
Olá mundo

Fatiamento [i:f:p] [::] #inicio : fim : passo
Obs: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(len(variavel[3]))
print((variavel[0:7]))
print(len(variavel))
print(variavel[::-1])