#blocos de código condicionais if / elif / else
#se / se não se / se não

#if = verificação de dado booleano True or False
#elif depende do if
#else depende do if também

entrada = input('Você quer "entrar" ou "sair" ')
if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair')