"""
Formatação básica de strings (fstrings ou format)
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes do 0
Sinal: + ou -
Ex.: 0 > -100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:&^10}.')
print(f'{1000.28432525:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')