nome = 'Yuri Oliveira Ramos'
altura = 1.73
peso = 64
imc = peso / (altura * 2) #IMC = peso / (altura x altura)

print(imc)
print(nome, 'tem', altura, 'metros de altura e pesa', peso, 'kg, logo seu IMC é:', imc)


#Atribuindo uma str a uma variável
#f-strings, f=formatação
linha_1 = f'{nome} tem {altura:.3f} metros de altura e pesa {peso} kg logo seu IMC é: {imc:.2f}'
print(linha_1)