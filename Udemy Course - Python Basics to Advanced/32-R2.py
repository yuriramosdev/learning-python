#Questão 2:
#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

horario = input('Digite o horário atual: ')

if horario.replace('.', '').isdigit():
    horario_float = float(horario)
    if horario_float >= 0 and horario_float <= 24:
        print(f'Agora são exatamente: {horario_float}.')
        if horario_float >= 0 and horario_float <= 11.59:
            print('Bom dia!')
        elif horario_float >= 12 and horario_float <= 17.59:
            print('Boa tarde!')
        elif horario_float >= 18 and horario_float <= 23.59: 
            print('Boa noite!')
    else:
        print('Digite um horário válido.')
else:
    print('Digite um horário válido.')

#--------------------------------------------------
    
# try:
#     horario_float = float(horario)
#     if horario_float >= 0 and horario_float <= 24:
#         print(f'Agora são exatamente: {horario_float}.')
#         if horario_float >= 0 and horario_float <= 11:
#             print('Bom dia!')
#         elif horario_float >= 12 and horario_float <= 17:
#             print('Boa tarde!')
#         elif horario_float >= 18 and horario_float <= 23.59:
#             print('Boa noite!')
#     else:
#         print('Digite um horário válido.')
# except:
#      print('Digite um horário válido.')