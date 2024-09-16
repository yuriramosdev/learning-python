#Operadores lógicos 
#and - or - not
#and - todas as condições precisam ser verdadeiras para que toda a expressão seja avaliada como verdadeira, caso haja um False, irá tratar tudo como False.
#or - inverso do and, caso haja um True, irá considerar o True na sentença.
#são consideradas falsy: 0 0.0 '' False
#Também existe o tipo None que é usado para representar um não valor
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S' or entrada == 's':
    print('Sair')
else:
    print('Digite um valor válido')
    senha_digitada = input()
"""
#A maneira certa de escrever o código é com while, visto que irá fazer checagens infinitas até dar certo.
    
#Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)