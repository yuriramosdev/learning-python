continuar = input('Deseja calcular o IMC de alguem? ')

while continuar == 'sim' or continuar == 'Sim':

    nome = input('\nQual o nome da pessoa? ')

    altura = input('Qual a altura dela? ')
    while not altura.replace('.','',1).isdigit():
        altura = input('Digite apanes numeros para a altura por favor: ')
        while not altura.replace('.','',1).isdigit():
            altura = input('Tente novamente: ')

    peso = input('Qual o peso dela? ')
    while not peso.replace('.','',1).isdigit():
        peso = input('Digite apanes numeros para o peso por favor: ')
        while not peso.replace('.','',1).isdigit():
            peso = input('Tente novamente: ')

    altura_float = float(altura)
    peso_float = float(peso)

    imc = peso_float / (altura_float * altura_float)

    print(f'A pessoa se chama {nome}, possui {altura_float:.2f} de altura e pesa {peso_float} kilos e seu IMC é {imc:.2f}\n')
    continuar = input('Deseja calcular o IMC de outra pessoa? ')

print('\nPrograma encerrado.')