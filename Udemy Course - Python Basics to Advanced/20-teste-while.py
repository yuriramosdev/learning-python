"""
x = input('Digite o número 2: ')

while x != '2':
    print('Digite um número seu animal...')
    x = input('Digite um valor novamente. ')
    
print(f'valor de X = {x}')
"""
x = input('Digite o numero inteiro positivo: ')

while x.isdigit() != True:
    print('Digite um numero, por favor...')
    x = input('Tente novamente: ')

print(f'O valor inteiro digitado foi: {x}')