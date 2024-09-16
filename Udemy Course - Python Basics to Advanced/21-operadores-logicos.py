#Operadores lógicos 
#and - or - not
#and - todas as condições precisam ser verdadeiras para que toda a expressão seja avaliada como verdadeira
#são consideradas falsy: 0 0.0 '' False
#Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S':
    print('Sair')
else:
    print('Digite um valor válido')