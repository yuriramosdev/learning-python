# Questão 3:
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome = input('Escreva seu nome: ')

if nome.replace(' ','').isalpha():
    if (len(nome)) <= 4:
        print('Seu nome é curto.')
    elif (len(nome)) == 5 or (len(nome)) == 6:
        print('Seu nome é normal.')
    elif (len(nome)) > 6:
        print('Seu nome é muito grande.')
else:
    print('Números não são válidos')
