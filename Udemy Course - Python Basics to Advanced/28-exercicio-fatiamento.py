"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {}
        Seu nome invertido é {}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {}
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
nome_sem_espaço = len(nome.replace(' ', ''))

if nome and idade:
    print(
        f'Seu nome é {nome};\n'
        f'Seu nome invertido é {nome_invertido};'
        )
    if ' ' in nome:
        print('Seu nome contém espaços;')
    else: 
        print('Seu nome não contém espaços;')

    print(f'Seu nome tem {nome_sem_espaço} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else: 
    print('Desculpe, você deixou os campos vazios.')