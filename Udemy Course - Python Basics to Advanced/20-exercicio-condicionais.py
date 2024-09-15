primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor} é maior do que o segundo valor {segundo_valor}.')
elif segundo_valor > primeiro_valor:
    print(f'Segundo valor {segundo_valor} é maior do que o primeiro valor {primeiro_valor}.')
elif primeiro_valor == ('') or segundo_valor == (''):
    print('Digite um valor.')
elif primeiro_valor == segundo_valor:
    print(f'Os números do primeiro valor {primeiro_valor} e do segundo valor {segundo_valor} são iguais')