#Questão 1:
#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.

numero_inteiro = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_inteiro)
    print('Você digitou um número inteiro.')

    if numero_int % 2 == 0:
        print('Você digitou um número par')
    else:
        print('Você digitou um número ímpar')
except:
    print('Você não digitou um número inteiro.')

# if numero_inteiro.isdigit():
#     print('Você digitou um número inteiro.')

#     numero_int = int(numero_inteiro)

#     if numero_int % 2 == 0:
#         print('Você digitou um número par')
#     else:
#         print('Você digitou um número ímpar')      
# else:
#     print('Você não digitou um número inteiro.')
